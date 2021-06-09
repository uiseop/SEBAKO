pragma solidity ^0.5.1;


contract ResumeNetwork{
    //STATE VARIABLES

    // smart contract 이름 명시
    string public name;

    // 이력서 총 개수
    uint public resumeCount;

    // 이력서안에 필수 내용들 확인 (API에선 이름, 자격번호만 확인)
    struct Resume{
        uint id;

        string title;
        string registerNumber;
        string issure;
        string date;
    }

    // 이력서 구조체를 연결함
    mapping(uint => Resume) public resumes;

    constructor() public{
        name='Resume On Blocks';
    }

    // 등록된 이력서 개수
    function get_count() view public returns(uint){
        return resumeCount;
    }

    //this function:
    // forSale부분을 (value값)True, False로 명시

    ///this function:
    // 새 이력서를 블럭에다 저장하기위해 모든 속성들을 유저한테 받아옴
    // 이력서를 mappings에 연결하여 블록을 연결
    // require구문을 통해 빠진부분이 없는지 확인,


    function createResume(string memory _title, string memory _registerNumber, string memory _issure, string memory _date) public{
        require(bytes(_title).length > 0);
        require(bytes(_registerNumber).length > 0);
        require(bytes(_issure).length > 0);
        require(bytes(_date).length > 0);

        resumeCount++;
        resumes[resumeCount] = Resume(resumeCount,_title,_registerNumber,_issure,_date);
    }

}

