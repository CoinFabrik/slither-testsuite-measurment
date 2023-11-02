# Slither Testsuite Mesaurement

| Example                                     | Class         | False positive/negative |
| :------------------------------------------ | :------------ | :---------------------- |
| [integer-underflow-1](#integer-underflow-1) | Arithmetic    | 0                       |
| [reentrancy-1](#reentrancy-1)               | Reentrancy    | 0                       |
| [reentrancy-2](#reentrancy-1)               | Reentrancy    | 0                       |
| [tx-origin](#tx-origin-1)                   | Authorization | 1                       |

---

## integer-underflow-1

### Configuration

Compiler version: 0.6.12

### Link to file

[examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol)

### Description

A simple vault in which users can deposit Ether, withdraw Ether and check their balances. Vulnerability is in withdraw function, [line 25](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L25).

(Adapted from [Source](https://github.com/serial-coder/solidity-security-by-example/tree/main/01_integer_underflow))

### Slither result

| Results | Correct | False Positive | False Negative |
| :------ | :------ | :------------- | :------------- |
| 6       | 6       | 0              | 0              |

#### Observations

- Integer overflow vulnerability detected by [tautology](https://github.com/crytic/slither/wiki/Detector-Documentation#tautology-or-contradiction) detector. Reported severity is Medium, should be High as an attacker could drain all contract Ethers in one transaction.
- [low-level-call](https://github.com/crytic/slither/wiki/Detector-Documentation#low-level-calls) warning is debatable (see [this](https://consensys.io/diligence/blog/2019/09/stop-using-soliditys-transfer-now/) article).
- Remaining results are some naming convetions and a comment on [solc-version](https://github.com/crytic/slither/wiki/Detector-Documentation#incorrect-versions-of-solidity) which is OK.

#### Checklist output

- [tautology](#tautology) (1 results) (Medium)
- [solc-version](#solc-version) (2 results) (Informational)
- [low-level-calls](#low-level-calls) (1 results) (Informational)
- [naming-convention](#naming-convention) (2 results) (Informational)

## tautology

Impact: Medium
Confidence: High

- [ ] ID-0
      [InsecureEtherVault.withdraw(uint256)](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L12-L20) contains a tautology or contradiction: - [require(bool,string)(balance - \_amount >= 0,Insufficient balance)](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L14)

examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L12-L20

## solc-version

Impact: Informational
Confidence: High

- [ ] ID-1
      Pragma version[0.6.12](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L3) allows old versions

examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L3

- [ ] ID-2
      solc-0.6.12 is not recommended for deployment

## low-level-calls

Impact: Informational
Confidence: High

- [ ] ID-3
      Low level call in [InsecureEtherVault.withdraw(uint256)](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L12-L20): - [(success) = msg.sender.call{value: \_amount}()](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L18)

examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L12-L20

## naming-convention

Impact: Informational
Confidence: High

- [ ] ID-4
      Parameter [InsecureEtherVault.getUserBalance(address).\_user](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L26) is not in mixedCase

examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L26

- [ ] ID-5
      Parameter [InsecureEtherVault.withdraw(uint256).\_amount](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L12) is not in mixedCase

examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L12

INFO:Slither:examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol analyzed (1 contracts with 93 detectors), 6 result(s) found

## reentrancy-1

### Configuration

Compiler version: 0.8.13

### Link to file

[examples/reentrancy/reentrancy-1.sol](examples/reentrancy/reentrancy-1.sol)

### Description

A simple vault in which users can deposit Ethers, withdraw Ethers, and check their balances. Vulnerability is in withdrawAll() function, [line 10](examples/reentrancy/reentrancy-1.sol#L10).

([Source](https://gist.github.com/serial-coder/5a29d95e1872c960950d4a00b36768e6#file-insecureethervault-sol))

### Slither result

| Results | Correct | False Positive | False Negative |
| :------ | :------ | :------------- | :------------- |
| 5       | 5       | 0              | 0              |

#### Observations

- Reentrancy vulnerability detected by [reentrancy-eth](https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities) detector.
- Remaining results are some naming conventions and a comment on [solc-version](https://github.com/crytic/slither/wiki/Detector-Documentation#incorrect-versions-of-solidity) which is OK.

#### Checklist output

Summary

- [reentrancy-eth](#reentrancy-eth) (1 results) (High)
- [solc-version](#solc-version) (2 results) (Informational)
- [low-level-calls](#low-level-calls) (1 results) (Informational)
- [naming-convention](#naming-convention) (1 results) (Informational)

## reentrancy-eth

Impact: High
Confidence: Medium

- [ ] ID-0
      Reentrancy in [InsecureEtherVault.withdrawAll()](examples/reentrancy/reentrancy-1.sol#L10-L18):
      External calls: - [(success) = msg.sender.call{value: balance}()](examples/reentrancy/reentrancy-1.sol#L14)
      State variables written after the call(s): - [userBalances[msg.sender] = 0](examples/reentrancy/reentrancy-1.sol#L17)
      [InsecureEtherVault.userBalances](examples/reentrancy/reentrancy-1.sol#L4) can be used in cross function reentrancies: - [InsecureEtherVault.deposit()](examples/reentrancy/reentrancy-1.sol#L6-L8) - [InsecureEtherVault.getUserBalance(address)](examples/reentrancy/reentrancy-1.sol#L24-L26) - [InsecureEtherVault.withdrawAll()](examples/reentrancy/reentrancy-1.sol#L10-L18)

examples/reentrancy/reentrancy-1.sol#L10-L18

## solc-version

Impact: Informational
Confidence: High

- [ ] ID-1
      Pragma version[0.8.13](examples/reentrancy/reentrancy-1.sol#L1) allows old versions

examples/reentrancy/reentrancy-1.sol#L1

- [ ] ID-2
      solc-0.8.13 is not recommended for deployment

## low-level-calls

Impact: Informational
Confidence: High

- [ ] ID-3
      Low level call in [InsecureEtherVault.withdrawAll()](examples/reentrancy/reentrancy-1.sol#L10-L18): - [(success) = msg.sender.call{value: balance}()](examples/reentrancy/reentrancy-1.sol#L14)

examples/reentrancy/reentrancy-1.sol#L10-L18

## naming-convention

Impact: Informational
Confidence: High

- [ ] ID-4
      Parameter [InsecureEtherVault.getUserBalance(address).\_user](examples/reentrancy/reentrancy-1.sol#L24) is not in mixedCase

examples/reentrancy/reentrancy-1.sol#L24

## reentrancy-2

### Configuration

Compiler version: 0.8.13

### Link to file

[examples/reentrancy/reentrancy-2.sol](examples/reentrancy/reentrancy-2.sol)

### Description

A toy contract showing a reentrancy that does not involve an ether transfer. Possible vulnerability is in the bug() function, [line 6](examples/reentrancy/reentrancy-2.sol#L6).
Adapted from ([Source](https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities-1))

### Slither result

| Results | Correct | False Positive | False Negative |
| :------ | :------ | :------------- | :------------- |
| 5       | 5       | 0              | 0              |

#### Observations

- Example built to trigger a different detector than the previous example.
- Reentrancy vulnerability correctly detected by [reentrancy-no-eth](https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities-1) detector.
- Remaining results are some naming conventions, low level call for call() usage, and a comment on [solc-version](https://github.com/crytic/slither/wiki/Detector-Documentation#incorrect-versions-of-solidity) which is OK.

#### Checklist output

Summary

- [reentrancy-no-eth](#reentrancy-no-eth) (1 results) (Medium)
- [solc-version](#solc-version) (2 results) (Informational)
- [low-level-calls](#low-level-calls) (1 results) (Informational)
- [naming-convention](#naming-convention) (1 results) (Informational)

## reentrancy-no-eth

Impact: Medium
Confidence: Medium

- [ ] ID-0
      Reentrancy in [PotentiallyInsecureReentrant.bug()](examples/reentrancy/reentrancy-2.sol#L6-L11):
      External calls: - [(success) = msg.sender.call()](examples/reentrancy/reentrancy-2.sol#L8)
      State variables written after the call(s): - [not_called = false](examples/reentrancy/reentrancy-2.sol#L10)
      [PotentiallyInsecureReentrant.not_called](examples/reentrancy/reentrancy-2.sol#L4) can be used in cross function reentrancies: - [PotentiallyInsecureReentrant.bug()](examples/reentrancy/reentrancy-2.sol#L6-L11) - [PotentiallyInsecureReentrant.not_called](examples/reentrancy/reentrancy-2.sol#L4)

examples/reentrancy/reentrancy-2.sol#L6-L11

## solc-version

Impact: Informational
Confidence: High

- [ ] ID-1
      Pragma version[0.8.13](examples/reentrancy/reentrancy-2.sol#L1) allows old versions

examples/reentrancy/reentrancy-2.sol#L1

- [ ] ID-2
      solc-0.8.13 is not recommended for deployment

## low-level-calls

Impact: Informational
Confidence: High

- [ ] ID-3
      Low level call in [PotentiallyInsecureReentrant.bug()](examples/reentrancy/reentrancy-2.sol#L6-L11): - [(success) = msg.sender.call()](examples/reentrancy/reentrancy-2.sol#L8)

examples/reentrancy/reentrancy-2.sol#L6-L11

## naming-convention

Impact: Informational
Confidence: High

- [ ] ID-4
      Variable [PotentiallyInsecureReentrant.not_called](examples/reentrancy/reentrancy-2.sol#L4) is not in mixedCase

examples/reentrancy/reentrancy-2.sol#L4

## tx-origin-1

### Configuration

Compiler version: 0.8.20

### Link to file

[examples/authorization/tx-origin-1/InsecureWallet.sol](examples/authorization/tx-origin-1/InsecureWallet.sol)

### Description

InsecureWallet is a simple contract with the intention that only the owner can transfer Ether to another address. Vulnerability is in line 13, when transfer function uses `tx.origin` to verify that the caller is indeed the owner.

(Adapted from [Source](https://solidity-by-example.org/hacks/phishing-with-tx-origin/))

### Slither result

| Results | Correct | False Positive | False Negative |
| :------ | :------ | :------------- | :------------- |
| 10      | 9       | 1              | 0              |

#### Observations

- High vulnerability reported by [arbitraty-send-eth](https://github.com/crytic/slither/wiki/Detector-Documentation#functions-that-send-ether-to-arbitrary-destinations) detector, which is right: there's an unprotected call to a function sending Ether to an arbitrary address (by a phishing with `tx.origin`).
- Medium vulnearability was also detected by [tx-origin](https://github.com/crytic/slither/wiki/Detector-Documentation#dangerous-usage-of-txorigin) detector, which is also right: it is not recommended to use `tx.origin` for authorization.
- Medium [erc20-interface](https://github.com/crytic/slither/wiki/Detector-Documentation#incorrect-erc20-interface) vulnerability is consider as false positive, since transfer function does not involve any token, just Ether.

- Low vulnerability of [missing-zero-check](https://github.com/crytic/slither/wiki/Detector-Documentation#missing-zero-address-validation) is OK.
- The remaining 3 Informational and 1 Optimization detectors are OK too.

#### Checklist output

- [arbitrary-send-eth](#arbitrary-send-eth) (1 results) (High)
- [erc20-interface](#erc20-interface) (1 results) (Medium)
- [tx-origin](#tx-origin) (1 results) (Medium)
- [missing-zero-check](#missing-zero-check) (1 results) (Low)
- [solc-version](#solc-version) (2 results) (Informational)
- [low-level-calls](#low-level-calls) (1 results) (Informational)
- [naming-convention](#naming-convention) (2 results) (Informational)
- [immutable-states](#immutable-states) (1 results) (Optimization)

## arbitrary-send-eth

Impact: High
Confidence: Medium

- [ ] ID-0
      [InsecureWallet.transfer(address,uint256)](examples/authorization/tx-origin-1/InsecureWallet.sol#L12-L17) sends eth to arbitrary user
      Dangerous calls: - [(sent) = \_to.call{value: \_amount}()](examples/authorization/tx-origin-1/InsecureWallet.sol#L15)

examples/authorization/tx-origin-1/InsecureWallet.sol#L12-L17

## erc20-interface

Impact: Medium
Confidence: High

- [ ] ID-1
      [InsecureWallet](examples/authorization/tx-origin-1/InsecureWallet.sol#L5-L18) has incorrect ERC20 function interface:[InsecureWallet.transfer(address,uint256)](examples/authorization/tx-origin-1/InsecureWallet.sol#L12-L17)

examples/authorization/tx-origin-1/InsecureWallet.sol#L5-L18

## tx-origin

Impact: Medium
Confidence: Medium

- [ ] ID-2
      [InsecureWallet.transfer(address,uint256)](examples/authorization/tx-origin-1/InsecureWallet.sol#L12-L17) uses tx.origin for authorization: [require(bool,string)(tx.origin == owner,Not owner)](examples/authorization/tx-origin-1/InsecureWallet.sol#L13)

examples/authorization/tx-origin-1/InsecureWallet.sol#L12-L17

## missing-zero-check

Impact: Low
Confidence: Medium

- [ ] ID-3
      [InsecureWallet.transfer(address,uint256).\_to](examples/authorization/tx-origin-1/InsecureWallet.sol#L12) lacks a zero-check on : - [(sent) = \_to.call{value: \_amount}()](examples/authorization/tx-origin-1/InsecureWallet.sol#L15)

examples/authorization/tx-origin-1/InsecureWallet.sol#L12

## solc-version

Impact: Informational
Confidence: High

- [ ] ID-4
      solc-0.8.20 is not recommended for deployment

- [ ] ID-5
      Pragma version[^0.8.20](examples/authorization/tx-origin-1/InsecureWallet.sol#L3) necessitates a version too recent to be trusted. Consider deploying with 0.8.18.

examples/authorization/tx-origin-1/InsecureWallet.sol#L3

## low-level-calls

Impact: Informational
Confidence: High

- [ ] ID-6
      Low level call in [InsecureWallet.transfer(address,uint256)](examples/authorization/tx-origin-1/InsecureWallet.sol#L12-L17): - [(sent) = \_to.call{value: \_amount}()](examples/authorization/tx-origin-1/InsecureWallet.sol#L15)

examples/authorization/tx-origin-1/InsecureWallet.sol#L12-L17

## naming-convention

Impact: Informational
Confidence: High

- [ ] ID-7
      Parameter [InsecureWallet.transfer(address,uint256).\_to](examples/authorization/tx-origin-1/InsecureWallet.sol#L12) is not in mixedCase

examples/authorization/tx-origin-1/InsecureWallet.sol#L12

- [ ] ID-8
      Parameter [InsecureWallet.transfer(address,uint256).\_amount](examples/authorization/tx-origin-1/InsecureWallet.sol#L12) is not in mixedCase

examples/authorization/tx-origin-1/InsecureWallet.sol#L12

## immutable-states

Impact: Optimization
Confidence: High

- [ ] ID-9
      [InsecureWallet.owner](examples/authorization/tx-origin-1/InsecureWallet.sol#L6) should be immutable

examples/authorization/tx-origin-1/InsecureWallet.sol#L6

INFO:Slither:examples/authorization/tx-origin-1/InsecureWallet.sol analyzed (1 contracts with 93 detectors), 10 result(s) found
