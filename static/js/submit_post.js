
const abi = [
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "bool",
				"name": "_forSale",
				"type": "bool"
			},
			{
				"internalType": "string",
				"name": "_title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_subtitle",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_content",
				"type": "string"
			}
		],
		"name": "createPost",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
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
	},
	{
		"constant": true,
		"inputs": [],
		"name": "postCount",
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
		"name": "posts",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "forSale",
				"type": "bool"
			},
			{
				"internalType": "uint256",
				"name": "tipAmount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "subtitle",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "content",
				"type": "string"
			},
			{
				"internalType": "address payable",
				"name": "author",
				"type": "address"
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
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "_value",
				"type": "bool"
			}
		],
		"name": "set_forSale",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "tipPost",
		"outputs": [],
		"payable": true,
		"stateMutability": "payable",
		"type": "function"
	}
]


// 수신 wallet_Address;
const c_address="0xE4cD403C1216cA0A313ed9419fD3d4C332EA818E";

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
        let content=$("#content").val();
        let for_sale=$("#for_sale").val();

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

                  contract.methods.createPost(sale,title,subtitle,content).send(
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
