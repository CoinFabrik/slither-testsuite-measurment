from slither.slither import Slither
from slither import *
from slither.detectors import all_detectors
from slither.printers import all_printers
from slither.detectors.abstract_detector import *
import json
import os


def extract_solc_version():
    pass


def result_comparison(run_out : dict(), exp_out : dict()):
    comparison_result = {"FOUND":0, "FALSE POSITIVE":0, "FALSE NEGATIVE":0}
    #check vulnerability. If any detectors triggered, CHECK
    #if no detectors triggered, all are false negatives
    if exp_out['vulnerable'] == True:
        pass
    else:
        #here the contract is not vulnerable. Anything found is a false positive
        # dict1 = key : value for (key, value) in run_out.items() if value is not []
        # comparison_result["FOUND"] = [1 for val in run_out.values() if len(val) != 0]
        comparison_result["FALSE NEGATIVE"] = comparison_result["FOUND"]

    #check function.
    #check detectors triggered.
    
    #count detectors triggered (FOUND)
    #count detectors not triggered (NOT FOUND)
    #count detectors found not in list (FALSE POSITIVE)
    #count detectors in list not found (FALSE NEGATIVE)
    print(run_out)
    print(exp_out)
    
    return comparison_result




all_detector_classes = dict([(name, cls) for name, cls in all_detectors.__dict__.items() if isinstance(cls, type)])
# high_detectors = dict([(name, cls) for name, cls in all_detector_classes if cls.IMPACT == DetectorClassification.HIGH])

slither_objects = {}
run_results = {}
expected_results = {}


for folder in os.listdir("examples"):

    #por ahora. Ver el tema de extraer el solc
    if (folder not in ["reentrancy-1", "reentrancy-2"]):
        continue

    contract_filepath = os.path.join("examples", folder, "contract.sol")
    expout_filepath = os.path.join("examples", folder, "expected-output.json")
    with open(expout_filepath) as expout:
        expected_results[folder] = json.load(expout)
    slither_objects[folder] = Slither(contract_filepath)


for example_name, slither_obj in slither_objects.items():
    for d in all_detector_classes.values():
        #uncomment to run only HIGH or MEDIUM impact detectors
            if d.IMPACT == DetectorClassification.HIGH or d.IMPACT == DetectorClassification.MEDIUM:
                slither_obj.register_detector(d)
    run_results[example_name] = slither_obj.run_detectors()


#run result comparison
for example_name, run_out in run_results.items():
    exp_out = expected_results[example_name]
    
    result_comparison(run_out, exp_out)



# slither = Slither("examples/reentrancy-1/contract.sol")


# for cls in all_detector_classes.values():
#     slither.register_detector(cls)
#     # slither.register_printer(all_printers.PrinterHumanSummary)

# slither_output = slither.run_detectors()
# for out in slither_output:
#     if len(out) != 0:
#         run_results.append(out)
# print(run_results)


# # f = open("package.json")
# # expected_output = json.load(f)
# # f.close()

# #compare expected_output with slither_output
# #...
# #...