
async function checkMeta(){
    if (typeof window.ethereum !== 'undefined'){
    window.web3 = new Web3(window.ethereum)
    await window.ethereum.enable()
    location.href = '/accounts/login/'
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

//const etherbtn = document.getElementById('etherbtn')
const ethereumButton = document.querySelector('.enableEthereumButton')
const showAccount = document.querySelector('#showAccount')
//const sendEthButton = document.querySelector('.sendEthButton')
//const showBalance = document.querySelector('.showBalance')
ethereumButton.addEventListener('click', () => {
  getAccount()
})

async function getAccount(){
  const accounts = await ethereum.request({method: 'eth_requestAccounts'})
  const account = accounts[0]
  console.log(account)
  console.log(account)
  console.log(account)
  console.log(account)
  console.log(account)
  showAccount.value = account
  console.log(showAccount)
  console.log(showAccount)

//  const balance = await ethereum
//  .request({
//    method: 'eth_getBalance',
//    params: [account,"latest"]
//  });
//  console.log(balance)
//  const read = parseInt(balance)/ 10**18
//  console.log(read.toFixed(5))
//  showBalance.innerText = read.toFixed(5)

  const value = 200
  console.log(value)


//  sendEthButton.addEventListener('click', () => {
//    ethereum
//      .request({
//        method: 'eth_sendTransaction',
//        params: [
//          {
//            from: account,
//            to: '0xE4cD403C1216cA0A313ed9419fD3d4C332EA818E',
//            value: Web3.utils.toHex(value)
//          }
//        ],
//      })
//      .then((txHash) => console.log(txHash))
//      .catch((error) => console.error)
//  })
}