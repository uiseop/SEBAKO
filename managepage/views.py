import asyncio
import json

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from web3 import Web3

url = 'https://ropsten.infura.io/v3/93d5193aae28437684c118ba0f6541d6'
web3 = Web3(Web3.HTTPProvider(url))
abi2 = json.loads('''[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "cid",
				"type": "address"
			}
		],
		"name": "newCareerCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "pid",
				"type": "address"
			}
		],
		"name": "newCertificationCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "eid",
				"type": "address"
			}
		],
		"name": "newEducationCreated",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "careerList",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "job",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "compName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "content",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "startDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "endDate",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "careeID",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "companyAddress",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "cidAvailable",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "companySignature",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "certificationList",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "certiName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "certiNumb",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "compName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "accDate",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "certiID",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "companyAddress",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "pidAvailable",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "companySignature",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "cidCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "cidList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "compAddressList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "companyCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "companyDetailList",
		"outputs": [
			{
				"internalType": "address",
				"name": "compAdress",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "compName",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "companyList",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companyRejectCaree",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companyRejectCerti",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companyRejectEdu",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companySignCaree",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companySignCerti",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companySignEdu",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "educationList",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "schoolName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "major",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "gpa",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "accDate",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "eduID",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "companyAddress",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "eidAvailable",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "companySignature",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "eidCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "eidList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "pidCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "pidList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_job",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_compName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_content",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_startDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_endDate",
				"type": "string"
			}
		],
		"name": "setCareerData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_certiName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_certiNumb",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_compName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_accDate",
				"type": "string"
			}
		],
		"name": "setCertificationData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_compAddress",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			}
		],
		"name": "setCompany",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_schoolName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_major",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_gpa",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_accDate",
				"type": "string"
			}
		],
		"name": "setEducationData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]''')
abi = json.loads('''[
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "string",
				"name": "_title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_registerNumber",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_company",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_dDate",
				"type": "string"
			}
		],
		"name": "createCertification",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "certificationCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "certifications",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "registerNumber",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "company",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "dDate",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "get_count",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]''')

certifi_address = '0xED111aBCE5A36F48bed94B18a995D78B4069f1b5'
contract_address = '0xCB8D8a589623d2DE83D1a5FfCE1759A5947a5F1d'
contract_address = web3.toChecksumAddress(contract_address)
certifi_address = web3.toChecksumAddress(certifi_address)

contract = web3.eth.contract(address=contract_address,abi=abi)
certifi_contract = web3.eth.contract(address=certifi_address,abi=abi2)


def getCompanyId():
    compIds = []
    count = certifi_contract.functions.companyCount().call()
    for i in range(count):
        compId = certifi_contract.functions.compAddressList(i+1).call()
        compIds.append(compId)
    return compIds

def getCertificationId():
    pidList = []
    count = certifi_contract.functions.pidCount().call()
    for i in range(count):
        pids = certifi_contract.functions.pidList(i+1).call()
        pidList.append(pids)
    return pidList

def getEducationId():
    eidList = []
    count = certifi_contract.functions.eidCount().call()
    for i in range(count):
        eids = certifi_contract.functions.eidList(i+1).call()
        eidList.append(eids)
    return eidList

def getCareerId():
    cidList = []
    count = certifi_contract.functions.cidCount().call()
    for i in range(count):
        cids = certifi_contract.functions.cidList(i+1).call()
        cidList.append(cids)
    return cidList

def base(request):
    compList = []
    compIds = getCompanyId()
    for compId in compIds:
        company = certifi_contract.functions.companyDetailList(compId).call()
        compList.append(company)

    context = {
        'companys':compList
    }
    return render(request,'accounts/home2.html',context)

def certifications(request):
    certificationList = []
    comps = getCompanyId()
    print(comps)
    pids = getCertificationId()
    print(pids)
    for pid in pids:
        certification = certifi_contract.functions.certificationList(pid).call()
        certificationList.append(certification)
    new_list = []
    for data in certificationList:
        new_list.append(data)
    context = {
        'certifications':new_list,
        'companys':comps
    }
    return render(request,'managepage/index.html',context)

def certificationDatabase(request,pk):
    # compList = []
    # compids = getCompanyId()
    #
    # for comp in compids:
    #     company = certifi_contract.functions.companyDetailList(comp).call()
    #     compList.append(company)
    # llList = []
    # for data in compList:
    #     llList.append(data)

    certificationList = []
    careerList = []
    educationList = []
    # pids = getCertificationId()
    # cids = getCareerId()
    # eids = getEducationId()
    # companyname = request.user.company.name
    # for pid in pids:
    #     certification = certifi_contract.functions.certificationList(pid).call()
    #     if certification[8] == False and certification[7] == True and certification[3] == companyname:
    #         certificationList.append(certification)

    # for cid in cids:
    #     career = certifi_contract.functions.careerList(cid).call()
    #     if career[9] == False and career[8] == True and career[2] == companyname:
    #         careerList.append(career)
    #
    # for eid in eids:
    #     education = certifi_contract.functions.educationList(eid).call()
    #     if education[8] == False and education[7] == True and education[1] == companyname:
    #         educationList.append(education)

    context = {
        "datas":certificationList,
        "cdatas":careerList,
        "edatas":educationList
    }
    return render(request, 'managepage/indexDetail.html',context)

def educationDatabase(request,pk):
    educationList = []
    eids = getEducationId()

    for eid in eids:
        education = certifi_contract.functions.educationList(eid).call()
        educationList.append(education)
    new_list = []
    for data in educationList:
        if data[8] == False:
            new_list.append(data)
        else:
            continue
    context = {
        "datas":new_list
    }
    return render(request, 'managepage/eduDetail.html',context)

def careerDatabase(request,pk):
    careerList = []
    cids = getEducationId()

    for cid in cids:
        career = certifi_contract.functions.careerList(cid).call()
        careerList.append(career)
    new_list = []
    for data in careerList:
        if data[8] == False:
            new_list.append(data)
        else:
            continue
    context = {
        "datas":new_list
    }
    return render(request, 'managepage/careerDetail.html',context)

def signCertification(request,pid):
    certification = certifi_contract.functions.certificationList(pid).call()
    comps = getCompanyId()
    context = {
        'pid':pid,
        'companys':comps
    }
    return render(request, 'managepage/index.html',context)
