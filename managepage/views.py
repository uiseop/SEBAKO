import json

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from web3 import Web3

url = 'https://ropsten.infura.io/v3/93d5193aae28437684c118ba0f6541d6'
web3 = Web3(Web3.HTTPProvider(url))

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

contract_address = '0xCB8D8a589623d2DE83D1a5FfCE1759A5947a5F1d'
contract_address = web3.toChecksumAddress(contract_address)

contract = web3.eth.contract(address=contract_address,abi=abi)
print(contract)

def waitingList(request):
    return render(request,'managepage/index.html')

def get_certifications_from_contract():
    contract_function = contract.functions['certificationCount']
    certificationCount = contract_function().call()

    certifications = []
    for i in range(certificationCount):
        cert = contract.functions.certifications(i+1).call()
        certifications.append(cert)
    return certifications

def certifications(request):

    cs = get_certifications_from_contract()

    cs.sort(key=lambda x:x[0])

    paginator = Paginator(cs,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'page':page_obj,
        'cs':cs
    }

    return render(request,'managepage/index.html',context)