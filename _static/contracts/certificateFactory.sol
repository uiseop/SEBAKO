// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/security/Pausable.sol";


contract certificateFactory is Ownable, Pausable{
    
    event CertificateCreated(address indexed _creator, address _certificate, uint256 _depositedValue);

    // call certificate.sol  && certificate 계약에 정의한 생성자는 주소를 인자로 받으므로 new Certificate. payable인자로 인해 Certificate 계약으로 계약을 만들면서 송금 가능
    function createCertificate() external payable whenNotPaused{
        Certificate certificate = new Certificate{value: msg.value}(msg.sender);
        emit CertificateCreated(msg.sender, address(certificate), msg.value);
    }
    
}