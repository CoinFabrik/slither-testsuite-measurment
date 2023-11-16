from slither.slither import Slither
from slither import *
from slither.detectors import all_detectors
from slither.printers import all_printers
from slither.detectors.abstract_detector import *
import json
import os
from solc_select import solc_select
import pprint


def solc_path_finder(version:str):
    if not solc_select.artifact_path(version).exists():
        print("Installing solc version", version)
        solc_select.install_artifacts([version])
    return solc_select.artifact_path(version).as_posix()


class_to_detector_mapping = {
    "Arithmetic":["divide-before-multiply", "tautological-compare", "tautology"],
    "Authorization":["tx-origin"],
    "Block attributes":["weak-prng"],
    "Delegate call":["controlled-delegatecall", "delegatecall-loop"],
    "DoS":[],
    "MEV":[],
    "Reentrancy":["reentrancy-eth", "reentrancy-no-eth"],
    "Privacy":[],
}


def result_comparison(run_out : dict(), exp_out : dict()):
    comparison_result = {"FOUND":0, "NOT FOUND":0, "FALSE POSITIVE":0, "FALSE NEGATIVE":0}
    mismatches = []

    #count detectors triggered
    triggered_detectors = [val for val in run_out if len(val) != 0]
    comparison_result["FOUND"] = len(triggered_detectors)

    #check vulnerability. If the contract is known to be vulnerable, we perform further checks
    if exp_out['vulnerable'] == True:
        triggered_detector_name_list = [val[0]['check'] for val in triggered_detectors]
        triggered_detector_functions = [val[0]['elements'][0]['name'] for val in triggered_detectors]
        expected_detector_name_list = class_to_detector_mapping[exp_out["class"]]
        
        #compute false positives
        for det_out in triggered_detectors:
            #first, we check that the functions match
            #if not, anything found is a false positive
            exp_function_name = exp_out['function']
            det_function_name = det_out[0]['elements'][0]['name']
            if (exp_function_name != det_function_name):
                mismatches.append({"EXPECTED FUNCTION": exp_function_name, "GOT FUNCTION": det_function_name})
                comparison_result["FALSE POSITIVE"] += 1
            else:
                #if functions match, check detectors
                if len(expected_detector_name_list) > 0 and det_out[0]['check'] not in expected_detector_name_list:
                    mismatches.append({"EXPECTED DETECTORS": expected_detector_name_list, "TRIGGERED DETECTOR": det_out[0]['check']})
                    comparison_result["FALSE POSITIVE"] += 1
        
        #compute false negatives
        # det_dif = list(set(expected_detector_name_list).difference(triggered_detector_name_list))
        if len(expected_detector_name_list) > 0: #and len(det_dif):
            #all expected detectors not triggered are false negatives
            # mismatches.append({"EXPECTED DETECTORS NOT TRIGGERED": det_dif})
            # comparison_result["FALSE NEGATIVE"] = len(det_dif)
            pass
        else:
            #if there are no expected detectors, we check if the vulnerable function is represented. If not, it's a false negative
            if exp_out['function'] in triggered_detector_functions:
                comparison_result["FALSE NEGATIVE"] = 0
            else:
                mismatches.append({"VULNERABLE FUNCTION NOT FLAGGED": exp_out['function']})
                comparison_result["FALSE NEGATIVE"] = 1

    else:
        #if the contract is not vulnerable, all found vulns. are false positives
        # note that for the purpose of this application we exclude informational and low impact detectors
        comparison_result["FALSE POSITIVE"] = comparison_result["FOUND"]
    
    #all false negatives are vulnerabilities not found
    comparison_result["NOT FOUND"] = comparison_result["FALSE NEGATIVE"]

    return (comparison_result, mismatches)




all_detector_classes = dict([(name, cls) for name, cls in all_detectors.__dict__.items() if isinstance(cls, type)])

slither_objects = {}
run_results = {}
expected_results = {}
files_to_run = []

#Traverse directories. For each contract: extract expected results and create the corresponding slither object (with the desired solc version)
for folder in os.listdir("examples"):
    for subfolder in os.listdir(os.path.join("examples", folder)):
        if (subfolder not in ['vulnerable', 'remediated']):
            continue

        contract_filepath = os.path.join("examples", folder, subfolder, "contract.sol")
        config_filepath = os.path.join("examples", folder, subfolder, "config.json")
        expout_filepath = os.path.join("examples", folder, subfolder, "expected-output.json")
        files_to_run.append(contract_filepath)
        
        with open(expout_filepath) as expout:
            expected_results[folder + " " + subfolder] = json.load(expout)
        
        solc_version = ""
        remaps = ""
        with open(config_filepath) as config_file:
            config = json.load(config_file)
            solc_version = config["solc"]
            if "dependencies" in config.keys():
                for dep in config["dependencies"]:
                    remaps += dep + '=node_modules/' + dep + ' '
        remaps = remaps[:-1]

        slither_objects[folder + " " + subfolder] = Slither(contract_filepath, solc = solc_path_finder(solc_version), solc_remaps = remaps)


for example_name, slither_obj in slither_objects.items():
    for d in all_detector_classes.values():
        #filter to run only HIGH or MEDIUM impact detectors
            if d.IMPACT == DetectorClassification.HIGH or d.IMPACT == DetectorClassification.MEDIUM:
                slither_obj.register_detector(d)
    run_results[example_name] = slither_obj.run_detectors()


#run result comparison
f = 0
for example_name, run_out in run_results.items():
    exp_out = expected_results[example_name]

    print(files_to_run[f])
    f += 1
    print(result_comparison(run_out, exp_out))
    print('\n')