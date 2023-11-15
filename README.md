# Slither Testsuite Mesaurement

Current database:

| Class            | Subclass                          | `examples/`              |
| :--------------- | :-------------------------------- | :----------------------- |
| Arithmetic       | Integer underflow                 | `integer-underflow-1`    |
| Authorization    | Tx origin                         | `tx-origin-1`            |
| Block attributes | Source of randomness              | `source-of-randomness-1` |
| Block attributes | Time manipulation                 | `time-manipulation-1`    |
| Delegate call    | Delegate call                     | `delegate-call-1`        |
| DoS              | Unexpected revert                 | `dos-1`                  |
| DoS              | Unexpected revert                 | `dos-2`                  |
| DoS              | Block gas limit                   | `dos-3`                  |
| MEV              | Front running                     | `mev-1`                  |
| Reentrancy       | Lack of CEI                       | `reentrancy-1`           |
| Reentrancy       | Lack of CEI                       | `reentrancy-2`           |
| Reentrancy       | Lack of CEI                       | `reentrancy-3`           |
| Privacy          | Unencrypted private data on-chain | `privacy-3`              |

Total examples: 13
