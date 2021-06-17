// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";

contract sebakoContract2 is Ownable{

    uint public pidCount;
    uint public cidCount;
    uint public eidCount;
    uint public companyCount;


    struct Certification{
        string name;
        string certiName;
        string certiNumb;
        string compName;
        string accDate;
        address certiID;
        address companyAddress;
        bool pidAvailable;
        bool companySignature;
    }

    struct Career{
        string name;
        string job;
        string compName;
        string content;
        string startDate;
        string endDate;
        address careeID;
        address companyAddress;
        bool cidAvailable;
        bool companySignature;
    }

    struct Education{
        string name;
        string schoolName;
        string major;
        string gpa;
        string accDate;
        address eduID;
        address companyAddress;
        bool eidAvailable;
        bool companySignature;
    }

    struct Company{
        address compAdress;
        string compName;
    }


    event newCertificationCreated(string name, address pid);
    event newCareerCreated(string name, address cid);
    event newEducationCreated(string name, address eid);

    mapping( address => bool) public companyList;
    mapping(uint => address) public pidList;
    mapping(uint => address) public cidList;
    mapping(uint => address) public eidList;
    mapping(uint => address) public compAddressList;
    mapping(address => Certification) public certificationList;
    mapping(address => Career) public careerList;
    mapping(address => Education) public educationList;
    mapping(address => Company) public companyDetailList;



    function getBalance() public view returns(uint){
        return address(this).balance;
    }

    //COMPANY FUNCTIONS
    function setCompany(address _compAddress,string memory _name) public onlyOwner{
        require(!companyList[_compAddress]);
        companyList[_compAddress] = true;
        companyDetailList[_compAddress].compAdress = _compAddress;
        companyDetailList[_compAddress].compName = _name;
        companyCount++;
        compAddressList[companyCount] = _compAddress;
    }

    function companySignCerti(address _pid) public{
        require(companyList[msg.sender]);
        certificationList[_pid].companySignature = true;
        certificationList[_pid].companyAddress = msg.sender;

    }

    function companyRejectCerti(address _pid) public{
        require(companyList[msg.sender]);
        certificationList[_pid].pidAvailable = false;
    }

    function companySignCaree(address _pid) public{
        require(companyList[msg.sender]);
        careerList[_pid].companySignature = true;
        careerList[_pid].companyAddress = msg.sender;

    }

    function companyRejectCaree(address _pid) public{
        require(companyList[msg.sender]);
        careerList[_pid].cidAvailable = false;
    }

    function companySignEdu(address _pid) public{
        require(companyList[msg.sender]);
        educationList[_pid].companySignature = true;
        educationList[_pid].companyAddress = msg.sender;

    }

    function companyRejectEdu(address _pid) public{
        require(companyList[msg.sender]);
        educationList[_pid].eidAvailable = false;

    }


    //CERTIFICATION FUNCTIONS
    function setCertificationData(string memory _name, string memory _certiName,string memory _certiNumb,string memory _compName,string memory _accDate) public{
        address pid = address(bytes20(keccak256(abi.encodePacked(msg.sender,block.timestamp))));
        certificationList[pid] = Certification(_name,_certiName,_certiNumb,_compName,_accDate,pid,0x0000000000000000000000000000000000000000,true,false);
        pidCount++;
        pidList[pidCount] = pid;

        emit newCertificationCreated(_name,pid);
    }

    //CAREER FUNCTIONS
    function setCareerData(string memory _name, string memory _job,string memory _compName,string memory _content,string memory _startDate, string memory _endDate) public{
        address cid = address(bytes20(keccak256(abi.encodePacked(msg.sender,block.timestamp))));
        careerList[cid] = Career(_name,_job,_compName,_content,_startDate,_endDate,cid,0x0000000000000000000000000000000000000000,true,false);

        cidCount++;
        cidList[cidCount] = cid;

        emit newCareerCreated(_name,cid);
    }

    //EDUCATION FUNCTIONS
    function setEducationData(string memory _name, string memory _schoolName,string memory _major,string memory _gpa,string memory _accDate) public{
        address eid = address(bytes20(keccak256(abi.encodePacked(msg.sender,block.timestamp))));
        educationList[eid] = Education(_name,_schoolName,_major,_gpa,_accDate,eid,0x0000000000000000000000000000000000000000,true,false);

        eidCount++;
        eidList[eidCount] = eid;

        emit newEducationCreated(_name,eid);
    }


}
