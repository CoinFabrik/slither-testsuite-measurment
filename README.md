# Slither Testsuite Mesaurement

| Example                                     | Class      | False positive/negative |
| :------------------------------------------ | :--------- | :---------------------- |
| [integer-underflow-1](#integer-underflow-1) | Arithmetic | 0                       |

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
- [low-level-call](https://github.com/crytic/slither/wiki/Detector-Documentation#low-level-calls) warning is okay in this case. However, if reentrancy modifier is removed, the tool keeps raising same informational low-level-call and does not recognice a possible reentrancy attack (false negative).
- Remaining results are some naming convetions and a comment on [solc-version](https://github.com/crytic/slither/wiki/Detector-Documentation#incorrect-versions-of-solidity) which is OK.

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
