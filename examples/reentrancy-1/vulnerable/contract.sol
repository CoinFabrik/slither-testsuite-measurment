// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

contract InsecureEtherVault {
    mapping (address => uint256) private userBalances;

    function deposit() external payable {
        userBalances[msg.sender] += msg.value;
    }

    function withdrawAll() external {
        uint256 balance = getUserBalance(msg.sender);
        require(balance > 0, "Insufficient balance");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Failed to send Ether");

        userBalances[msg.sender] = 0;
    }

    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    function getUserBalance(address _user) public view returns (uint256) {
        return userBalances[_user];
    }
}

/*
Reentrancy  

A simple vault in which users can deposit Ether, withdraw Ether, 
and check their balances. Vulnerability is in withdrawAll function, 
as there's no check-effects-interaction pattern.

Source https://gist.github.com/serial-coder/5a29d95e1872c960950d4a00b36768e6#file-insecureethervault-sol
*/