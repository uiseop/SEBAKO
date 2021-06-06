// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/security/Pausable.sol";
import "./activatable.sol";

contract Certificate is Ownable, Pausable, Activatable{
    uint public cCount;
    // is Owanble 계약을 상속함. Ownable 계약의 상태변수 _owner을 사용함
    address _owner = owner();
    
    mapping(uint => certification) public pidList;
    // mapping (uint256 => bool) public rewardSent;
    event Deposit(address indexed _depositor, uint256 _depositValue);
    // event RewardSent(address indexed _dest, uint256 _reward, uint256 _id);
    event RefundedToOwner(address indexed _dest, uint256 _refundedBalance);
    
    // CertificateFactory계약에서 실행. payable이라는 함수 제한자는 계약 생성과 동시에 certificate 계약에 송금하는 상황이 발생.
    //_owner 변수는 address 타입의 실제 인자 _creator가 할당 _creator에는 계약을 만든 사용자의 주소를 저장
    constructor(address _creator) payable{
        _owner = _creator;
    }
    
    struct certification{
        
        string title;
        string rNumber;
        string company;
        string dDate;
        
        bool sign;
    }
    
    function setCertification(string memory _title, string memory _rNumber,string memory _company, string memory _dDate) external payable{
        cCount++;
        pidList[cCount] = certification(_title,_rNumber,_company,_dDate,false);
    }
    
    function deposit() external payable whenNotPaused{
        require(msg.value > 0, "");
        emit Deposit(msg.sender, msg.value);
    }
    
    // 계약의 소유자 이외에는 보상을 지급할 수 없도록 제한함.
    // address타입의 _dest를 address payable타입으로 전환
    // function sendReward(uint256 _reward, address payable _dest, uint256 _id) external onlyOwner{
    //     require(!rewardSent[_id],"");
    //     require(_reward>0,"");
    //     require(address(this).balance >= _reward,"");
    //     require(_dest != address(0), "");
    //     require(_dest != _owner,"");
        
    //     rewardSent[_id] = true;
    //     _dest.transfer(_reward);
    //     emit RewardSent(_dest, _reward, _id);
    // }
    
    // 계약을 중단시 남은 이더를 소유자에게 반환하는 함수. 역시 소유자만 이더 반환을 실행할수 있음
    function refundToOwner() external onlyOwner{
        require(address(this).balance>0,"");
        uint256 refundedBalance = address(this).balance;
        // address(uint160(_owner)).transfer(address(this).balance);
        address payable newspender = payable(_owner);
        newspender.transfer(refundedBalance);
        emit RefundedToOwner(msg.sender,refundedBalance);
    }
}