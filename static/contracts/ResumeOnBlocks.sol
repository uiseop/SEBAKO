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

        // forSale 부분은 자격증공단에서 확인해주기위한 키로 사용
        bool forSale;
        uint tipAmount;
        string title;
        string registerNumber;
        string issure;
        string date;
        address payable author;
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

    function set_forSale(uint _id, bool _value) public{
        Resume memory _resume = resumes[_id];
        _resume.forSale=_value;
        resumes[_id]=_resume;
    }

    ///this function:
    // 새 이력서를 블럭에다 저장하기위해 모든 속성들을 유저한테 받아옴
    // 이력서를 mappings에 연결하여 블록을 연결
    // require구문을 통해 빠진부분이 없는지 확인,


    function createResume(bool _forSale,string memory _title, string memory _registerNumber, string memory _issure, string memory _date) public{
        require(bytes(_title).length > 0);
        require(bytes(_registerNumber).length > 0);
        require(bytes(_issure).length > 0);
        require(bytes(_date).length > 0);

        resumeCount++;
        resumes[resumeCount] = Resume(resumeCount,_forSale,0,_title,_registerNumber,_issure,_date,msg.sender);
    }

    ///this function:
    // 이력서의 id를 선택함
    // 자격공단에서 해당 이력서에 대한 공증 (db를 사용하여 하면 되지만 시각적 효과를 주기위해 클릭옵션 구현)
    // ether를 송금하여 해당 트렌젝션이 발생하도록 함
    // mapping에 추가하여 블록을 연결

    function tipResume(uint _id) payable public{
        Resume memory _resume = resumes[_id];
        address payable _author = _resume.author;
        address (_author).transfer(msg.value);
        _resume.tipAmount = _resume.tipAmount+msg.value;
        resumes[_id] = _resume;


    }
}

