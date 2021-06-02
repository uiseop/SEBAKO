const abi = [
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
		"name": "newCertifiactionCreated",
		"type": "event"
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
		"name": "compAddressList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "companyCount",
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
			},
			{
				"internalType": "string",
				"name": "compSpecialization",
				"type": "string"
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
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companySign",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getBalance",
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
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "pidCount",
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
		"name": "pidList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
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
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "resumeList",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "registerNumber",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "companyName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "issueDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "fileurl",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "companyAddress",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "resumeID",
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
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_registerNumber",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_companyName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_issueDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_fileurl",
				"type": "string"
			}
		],
		"name": "setCertifiactionData",
		"outputs": [],
		"payable": true,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": false,
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
			},
			{
				"internalType": "string",
				"name": "_spec",
				"type": "string"
			}
		],
		"name": "setCompany",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "address",
				"name": "_newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
// 수신 wallet_Address;
const c_address="0xE4cD403C1216cA0A313ed9419fD3d4C332EA818E";
const cc_address="0xEF877539c18F3F0149B5C08acBa5938D77552d57";

async function checkMeta(){
    if (typeof window.ethereum !== 'undefined'){
    window.web3 = new Web3(window.ethereum)
    web3 = window.web3
    await window.ethereum.enable()
//    location.href = '/accounts/login/'
//      alert('MetaMask가 설치되었습니다!')
//      console.log('MetaMask가 설치되었습니다!')
    }else{
      var conf = confirm('MetaMask 프로그램이 없으시군요?\n설치하시겠습니까?')
      if(conf){
        location.href = "https://chrome.google.com/webstore/detail/nkbihfbeogaeaoehlefnkodbefgpgknn"
      }
      else{

      }
      console.log('MetaMask를 설치하십시오')
      document.querySelector('.enableEthereumButton').innerHTML = "<a href='https://chrome.google.com/webstore/detail/nkbihfbeogaeaoehlefnkodbefgpgknn'>"
      document.querySelector('.intro').getElementsByClassName.display = 'none'

    }
}

async function loadCertificateData(){
    window.web3 = new Web3(window.ethereum)
    const ww3 = window.web3
    await window.ethereum.enable()
    const wallet = await ww3.eth.getAccounts();
    console.log(wallet)
    console.log(wallet)
    console.log(wallet)
    const certificateContract = new ww3.eth.Contract(abi,cc_address)
    const certificateCount = await certificateContract.methods.get_count().call()
}

window.onload = loadCertificateData()

// 화면 들어오면 바로 실행되게 함
window.addEventListener('load', checkMeta()
);


contract = new web3.eth.Contract(abi,c_address)

function waitForReceipt(hash, cb) {
    web3.eth.getTransactionReceipt(hash, function (err, receipt) {
      if (err) {
        error(err);
      }
      if (receipt !== null) {
        // Transaction went through
        if (cb) {
          cb(receipt);
        }
      } else {
        // Try again in 1 second
        window.setTimeout(function () {
          waitForReceipt(hash, cb);
        }, 1000);
      }
    });
  }
      //FOR CHANGING PAGE
      function append(){
        $("#rec_url").text("RECEIPT IS LOADING......")
        var sale;
        let title=$("#title").val();
        let subtitle=$("#subtitle").val();
        let company=$("#content").val();
        let ddate = $("#ddate").val();
        let filehash = $("#image_hash").val();

        if(for_sale == 'on'){
          sale = true;
        }
        else{
          sale = false;
        }
        web3.eth.getAccounts(function get(err, res){
                  account=res[0]
                  console.log(account)
                  transaction =
                  ({
                    from: account,
                    "gas": 300000,
                    "chainId": 3,
                    "gasPrice": web3.utils.toWei('4.1','Gwei')
                  })

                  contract.methods.setCertifiactionData(title,subtitle,company,ddate,filehash).send(
                      transaction,
                      (error,result)=>{
                          if(error){
                            console.log('hahah why not')
                          }
                          else{
                            waitForReceipt(result, function(){
                                console.log(result)
                                var newUrl = "https://ropsten.etherscan.io/tx/" + result
                                $("#rec_url").attr("href", newUrl)
                                $("#rec_url").text(result)
                                }
                            )
                          }
                      }
                  );

        });

      }
