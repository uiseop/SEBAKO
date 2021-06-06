// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";

contract Activatable is Ownable{
    event Deactivate(address indexed _sender);
    event Activate(address indexed _sender);
    
    bool public active = false;
    
    modifier whenActive(){
        require(active,"");
        _;
    }
    
    modifier whenNotActive(){
        require(!active,"");
        _;
    }
    
    function deactivate() public whenActive onlyOwner{
        active = false;
        emit Deactivate(msg.sender);
    }
    
    function activate() public whenNotActive onlyOwner{
        active = true;
        emit Activate(msg.sender);
    }
}