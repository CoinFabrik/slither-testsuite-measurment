pragma solidity 0.8.13;

contract PotentiallyInsecureReentrant {
    bool public not_called;

    function bug() public{
        require(not_called);
        (bool success, ) = msg.sender.call("");
        require(success, "Failed to call");
        not_called = false;
    }
}