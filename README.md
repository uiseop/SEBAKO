<img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/Web3-F16822?style=flat-square&logo=Web3%2Ejs&logoColor=white"/> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/> <img src="https://img.shields.io/badge/Ethereum-3C3C3D?style=flat-square&logo=Ethereum&logoColor=white"/> <img src="https://img.shields.io/badge/MetaMask-F77E1C?style=flat-square&logo=Metamask&logoColor=white"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/> <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=Amazon%20AWS&logoColor=white"/>

# 블록체인을 활용한 안심이력관리 시스템
> 동국대학교 정보통신공학과 SEBAKO팀
<hr/>

## 프로젝트 목표
본 프로젝트는 이더 리움을 기반으로 구축 된 분산 형 애플리케이션으로, 제 3 자의 개입없이 최고의 효율성으로 사용자에게 개인이 입증하기 쉽지않은 다양한 경험 및 자격들에 대해 인증을 해줌으로써 투명하고 신뢰할 수 있도록 보장함으로써 문서 및 자격증의 진위에 대한 솔루션을 제공하는 것을 목표로합니다.

## 현재 인증시스템의 문제점
1. 중앙집중형 스토리지의 문제점 (스토리지의 중앙화의 위험)
2. 개인이 인증을 위해 추가적인 절차 및 비용의 발생
3. 2의 문제점으로 인해 위변조에 취약

자격증을 예로 들면 자격증 취득 -> 개인 자기소개서 작성시 기입 -> 기업에서 자격증 진위를 위한 정부24에 문의하는 기업에서 추가적인 인증절차를 필요로 함. 

자격증을 취득하는 동시에 블록체인에 해당 정보를 등록시켜두면 기업에서 자격증 진위 확인을 위해 추가적인 인증절차가 필요하지 않게됨.

## SEBAKO의 주요 솔루션
* 탈중앙화 : SEBAKO팀은 자격증 발행 및 경력 인증시스템 더 나아가 인증이 필요한 모든 물품 상품의 인증에 관련된 제 3자 및 중앙처리기관의 문제를 해결합니다.
* 스마트 계약 : 제 3자의 간섭없이 서로 다른 당사자 간의 모든 인증을 처리합니다. 
* 블록체인 : 블록체인에 있는 모든 거래의 모든 세부사항을 저장하고 변경할수 없도록 합니다.

## SEBAKO 기능들
* **관리자**는 블록체인에 새로운 기업을 추가 할 수 있습니다.
* **기업회원**은 해당 기업이름으로 요청된 인증사항들(자격증, 경력, 학력)에 대해 승인/거절을 할 수 있습니다. 혹은 API를 지원하여 자동으로 처리가 되도록 요청할수 있습니다.
* **개인회원**은 개인의 인증받고싶은 사항들에 대해 요청을 보낼 수 있고, 등록된 개인지갑을 활용해 요청에 대한 처리 결과를 확인할 수 있습니다.

## 사용방법
1. Metamask 설치 및 개인지갑 생성

![image](https://user-images.githubusercontent.com/75655047/121512081-4e867480-ca24-11eb-8d90-5110de64238b.png)

2. Metamask 실행 -> Ropsten 테스트 네트워크에 연결 -> 구매 ->  포시트 테스트에서 Ether얻기(계약 요청시에 필요)

![image](https://user-images.githubusercontent.com/75655047/121511130-4aa62280-ca23-11eb-8854-f1856ea48504.png)
3. 회원가입 및 개인 프로필 작성
4. 등록된 기관목록을 확인하고 요청을 보내기
