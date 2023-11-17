# Slither Testsuite Mesaurement

Current database:

| Class            | Subclass                          | `examples/`          |
| :--------------- | :-------------------------------- | :------------------- |
| Arithmetic       | Integer underflow                 | `arithmetic-1`       |
| Authorization    | Tx origin                         | `authorization-1`    |
| Authorization    | Delegate call                     | `authorization-2`    |
| Block attributes | Source of randomness              | `block-attributes-1` |
| Block attributes | Time manipulation                 | `block-attributes-2` |
| DoS              | Unexpected revert                 | `dos-1`              |
| DoS              | Unexpected revert                 | `dos-2`              |
| DoS              | Block gas limit                   | `dos-3`              |
| DoS              | Block gas limit                   | `dos-4`              |
| MEV              | Front running                     | `mev-1`              |
| Privacy          | Unencrypted private data on-chain | `privacy-3`          |
| Reentrancy       | Lack of CEI                       | `reentrancy-1`       |
| Reentrancy       | Lack of CEI                       | `reentrancy-2`       |
| Reentrancy       | Lack of CEI                       | `reentrancy-3`       |

Total examples: 14
