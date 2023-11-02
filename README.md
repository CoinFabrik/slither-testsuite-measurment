# Slither Testsuite Mesaurement

| Example                                     | Class      | False positive/negative |
| :------------------------------------------ | :--------- | :---------------------- |
| [integer-underflow-1](#integer-underflow-1) | Arithmetic | 0                       |
| [reentrancy-1](#reentrancy-1)               | Reentrancy | 0                       |
| [reentrancy-2](#reentrancy-1)               | Reentrancy | 0                       |

---

## integer-underflow-1

### Configuration

Compiler version: 0.6.12

### Link to file

[examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol)

### Description

A simple vault in which users can deposit Ethers, withdraw Ethers, and check their balances. Vulnerability is in withdraw function, [line 25](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L25).

([Source](https://github.com/serial-coder/solidity-security-by-example/tree/main/01_integer_underflow))

### Slither result

| Results | Correct | False Positive | False Negative |
| :------ | :------ | :------------- | :------------- |
| 6       | 6       | 0              | 0              |

#### Observations

- Integer overflow vulnerability detected by [tautology](https://github.com/crytic/slither/wiki/Detector-Documentation#tautology-or-contradiction) detector. Reported severity is Medium, should be High as an attacker could drain all contract Ethers in one transaction.
- [low-level-call](https://github.com/crytic/slither/wiki/Detector-Documentation#low-level-calls) warning is okay in this case. However, if reentrancy modifier is removed, the tool keeps raising same informational low-level-call and does not recognize a possible reentrancy attack (false negative).
- Remaining results are some naming conventions and a comment on [solc-version](https://github.com/crytic/slither/wiki/Detector-Documentation#incorrect-versions-of-solidity) which is OK.

#### Checklist output

- [tautology](#tautology) (1 results) (Medium)
- [solc-version](#solc-version) (2 results) (Informational)
- [low-level-calls](#low-level-calls) (1 results) (Informational)
- [naming-convention](#naming-convention) (2 results) (Informational)

##### tautology

Impact: Medium
Confidence: High

- [ ] ID-0
      [InsecureEtherVault.withdraw(uint256)](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L23-L31) contains a tautology or contradiction:
  - [require(bool,string)(balance - \_amount >= 0,Insufficient balance)](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L25)

InsecureEtherVault.sol#L23-L31

##### solc-version

Impact: Informational
Confidence: High

- [ ] ID-1
      Pragma version[0.6.12](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L3) allows old versions

InsecureEtherVault.sol#L3

- [ ] ID-2
      solc-0.6.12 is not recommended for deployment

##### low-level-calls

Impact: Informational
Confidence: High

- [ ] ID-3
      Low level call in [InsecureEtherVault.withdraw(uint256)](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L23-L31): - [(success) = msg.sender.call{value: \_amount}()](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L29)

InsecureEtherVault.sol#L23-L31

##### naming-convention

Impact: Informational
Confidence: High

- [ ] ID-4
      Parameter [InsecureEtherVault.getUserBalance(address).\_user](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L37) is not in mixedCase

InsecureEtherVault.sol#L37

- [ ] ID-5
      Parameter [InsecureEtherVault.withdraw(uint256).\_amount](examples/arithmetic/integer-underflow-1/InsecureEtherVault.sol#L23) is not in mixedCase

InsecureEtherVault.sol#L23

INFO:Slither:InsecureEtherVault.sol analyzed (2 contracts with 93 detectors), 6 result(s) found


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
        External calls:
        - [(success) = msg.sender.call{value: balance}()](examples/reentrancy/reentrancy-1.sol#L14)
        State variables written after the call(s):
        - [userBalances[msg.sender] = 0](examples/reentrancy/reentrancy-1.sol#L17)
        [InsecureEtherVault.userBalances](examples/reentrancy/reentrancy-1.sol#L4) can be used in cross function reentrancies:
        - [InsecureEtherVault.deposit()](examples/reentrancy/reentrancy-1.sol#L6-L8)
        - [InsecureEtherVault.getUserBalance(address)](examples/reentrancy/reentrancy-1.sol#L24-L26)
        - [InsecureEtherVault.withdrawAll()](examples/reentrancy/reentrancy-1.sol#L10-L18)

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
Low level call in [InsecureEtherVault.withdrawAll()](examples/reentrancy/reentrancy-1.sol#L10-L18):
        - [(success) = msg.sender.call{value: balance}()](examples/reentrancy/reentrancy-1.sol#L14)

examples/reentrancy/reentrancy-1.sol#L10-L18


## naming-convention
Impact: Informational
Confidence: High
 - [ ] ID-4
Parameter [InsecureEtherVault.getUserBalance(address)._user](examples/reentrancy/reentrancy-1.sol#L24) is not in mixedCase

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
        External calls:
        - [(success) = msg.sender.call()](examples/reentrancy/reentrancy-2.sol#L8)
        State variables written after the call(s):
        - [not_called = false](examples/reentrancy/reentrancy-2.sol#L10)
        [PotentiallyInsecureReentrant.not_called](examples/reentrancy/reentrancy-2.sol#L4) can be used in cross function reentrancies:
        - [PotentiallyInsecureReentrant.bug()](examples/reentrancy/reentrancy-2.sol#L6-L11)
        - [PotentiallyInsecureReentrant.not_called](examples/reentrancy/reentrancy-2.sol#L4)

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
Low level call in [PotentiallyInsecureReentrant.bug()](examples/reentrancy/reentrancy-2.sol#L6-L11):
        - [(success) = msg.sender.call()](examples/reentrancy/reentrancy-2.sol#L8)

examples/reentrancy/reentrancy-2.sol#L6-L11


## naming-convention
Impact: Informational
Confidence: High
 - [ ] ID-4
Variable [PotentiallyInsecureReentrant.not_called](examples/reentrancy/reentrancy-2.sol#L4) is not in mixedCase

examples/reentrancy/reentrancy-2.sol#L4