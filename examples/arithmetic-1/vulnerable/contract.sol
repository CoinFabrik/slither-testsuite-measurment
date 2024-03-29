// SPDX-License-Identifier: MIT
pragma solidity 0.6.12;

contract InsecureEtherVault {
    mapping (address => uint256) private userBalances;

    function deposit() external payable {
        userBalances[msg.sender] += msg.value;
    }

    function withdraw(uint256 _amount) external {
        uint256 balance = getUserBalance(msg.sender);
        require(balance - _amount >= 0, "Insufficient balance");

        userBalances[msg.sender] -= _amount;
        
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Failed to send Ether");
    }

    function getEtherBalance() external view returns (uint256) {
        return address(this).balance;
    }

    function getUserBalance(address _user) public view returns (uint256) {
        return userBalances[_user];
    }
}

/*
Arithmetic - Integer Underflow 

A simple vault in which users can deposit Ether, withdraw Ether and check their
balances. Vulnerability is in withdraw function, line 13.

Adapted from https://github.com/serial-coder/solidity-security-by-example/tree/main/01_integer_underflow
*/
