// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

contract ParticularVault {
    struct Payee {
        address addr;
        uint256 value;
    }

    Payee[] payees;
    uint256 nextPayeeIndex;

    function deposit() external payable {
        payees.push(Payee(msg.sender, msg.value));
    }

    function payOut() external {
        uint256 i = nextPayeeIndex;
        while (i < payees.length) {
            payable(payees[i].addr).transfer(payees[i].value);
            i++;
        }
        nextPayeeIndex = i;
    }
}

/*
DoS - Gas limit via Unbounded Operations

In this particular vault, people can deposit and there's a pay out function 
which pays them all.

By paying out to everyone at once, it risks running into the 
block gas limit.

This can lead to problems even in the absence of an intentional attack. However, 
it's especially bad if an attacker can manipulate the amount of gas needed. In the 
case of the previous example, the attacker could add a bunch of addresses, each of 
which needs to get a very small refund. The gas cost of refunding each of the 
attacker's addresses could, therefore, end up being more than the gas limit, blocking the 
refund transaction from happening at all.

It also has:
    - DoS unexpected revert vulnerability due to the push logic (see dos-1 or dos-2)
    - Reentrancy but limited by transfer limited amount of gas

Adapted from https://consensys.github.io/smart-contract-best-practices/attacks/denial-of-service/#dos-with-block-gas-limit
*/
