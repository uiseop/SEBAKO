function startLogin() {
  if (typeof web3 !== 'undefined') {
    checkWeb3(function (loggedIn) {
      if (!loggedIn) {
        alert("Please unlock your web3 provider (probably, Metamask)")
      } else {
        var login_url = '{% url 'web3auth_login_api' %}';
        web3Login(login_url, console.log, console.log, console.log, console.log, console.log, function (resp) {
          console.log(resp);
          window.location.replace(resp.redirect_url);
        });
      }
    });

  } else {
    alert('web3 missing');
  }
}