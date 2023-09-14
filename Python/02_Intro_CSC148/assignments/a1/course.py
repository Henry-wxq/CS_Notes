<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset='UTF-8'>
<meta http-equiv='X-UA-Compatible' content='IE=Edge'>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="MemzEr8vWUB1viIT3cblg6kKHT6kwVqsr99MJWC2sHHzVoDCAChsjhxgZUSvqkjrQpq0X8oWk4ob9e1o9UPlqw" />
<meta name="csp-nonce" content="tplycHS22DbDN5emptYOEA==" />
<link rel="stylesheet" href="/2023-01/assets/application-287b27f62077446144055e6468ad6f3717505820543c64bf019e865f1699e5f1.css" />
<link rel="icon" type="image/x-icon" href="/2023-01/assets/favicon-7c1c4e00b6ae699747f28ec49b8bc701dac0f7b74788644603390e7dfacb1775.ico" />
<script nonce="tplycHS22DbDN5emptYOEA==">
//<![CDATA[
const AUTH_TOKEN = document.querySelector('[name="csrf-token"]').content;
//]]>
</script>
<script nonce="tplycHS22DbDN5emptYOEA==">
//<![CDATA[

  const MARKUS_VERSION = 'v2.2.1';

//]]>
</script>
  <title>MarkUs - login</title>
    <script src="/2023-01/assets/cookies_eu-8953875e8bccb488206cfcd6f8a79fd6eacfbd1aaf08f2108b8c1c2fd39061fa.js" nonce="tplycHS22DbDN5emptYOEA=="></script>
  <script nonce="tplycHS22DbDN5emptYOEA==">
//<![CDATA[

    document.addEventListener('DOMContentLoaded', () => {
      document.getElementById('local-login-selector').addEventListener('click', () => {
        const formElem = document.getElementById('local-login-form');
        if (getComputedStyle(formElem).display === 'none') {
          formElem.style.display = 'block';
        } else {
          formElem.style.display = 'none';
        }
      })
    })

//]]>
</script>
</head>
<body>
  
<main class='login'>
  <div class='login-image'></div>

  <div class='login-error'>
     <!-- keep this line until issue #3342 has been resolved (somehow it fixes it) -->
    <div class="notice no-display">
      <a class="hide-flash">&nbsp;</a>
      <div class="flash-content"></div>
    </div>
    <div class="error">
      <a class="hide-flash">&nbsp;</a>
      <div class="flash-content">
          <p><p>Authentication with your UTORid and password (students only) was successful but no corresponding user was found in the MarkUs database.</p></p>
      </div>
    </div>
    <div class="success no-display">
      <a class="hide-flash">&nbsp;</a>
      <div class="flash-content"></div>
    </div>
    <div class="warning no-display">
      <a class="hide-flash">&nbsp;</a>
      <div class="flash-content"></div>
    </div>
<script nonce="tplycHS22DbDN5emptYOEA==">
//<![CDATA[

  // using addEventListener as opposed to direct assignment so that event listeners added elsewhere
  // don't get overridden
  window.addEventListener("DOMContentLoaded", function () {
    Array.from(document.getElementsByClassName('hide-flash')).forEach(function (elem) {
      elem.addEventListener("click", function(e) {
        e.target.parentElement.style.display = 'none';
      })
    })
  })

//]]>
</script>
  </div>

  <div class='login-form'>
        <div class="login-selector">
          <a class="button" id="local-login-selector">Log in with your teach.cs user name and password</a>
        </div>
      <form id="local-login-form" class="no-display" action="/2023-01/?locale=en" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="_JVmG01MX8aR_V58RIgpQWJvOtyLEAIfVDqgW97ugpfUelXe2t03cXILSngrgY_MUFtn1DTtgMy8Sd8t1LISrA" autocomplete="off" />
        <input type="text" name="user_login" id="user_login" value="" placeholder="User Name" aria-label="User Name" autocorrect="off" autocapitalize="off" autofocus="autofocus" />
        <input type="password" name="user_password" id="user_password" placeholder="Password" aria-label="Password" autocomplete="off" />
        <div class='submit'>
          <input type="submit" name="commit" value="Log in" data-disable-with="Logging in..." />
        </div>
</form>        <div id='login-or-container'><h4 id="login-or">OR</h4></div>
      <div class="login-selector">
        <a
          class="button"
          href="/2023-01/main/login_remote_auth?locale=en"
        >Log in with your UTORid and password (students only)</a>
      </div>
  </div>
</main>

    <div class="cookies-eu js-cookies-eu" >
      <span class="cookies-eu-content-holder">Cookies help us deliver our services. By using our services, you agree to our use of cookies.</span>
      <span class="cookies-eu-button-holder">
      <button class="cookies-eu-ok js-cookies-eu-ok"> OK </button>
      </span>
    </div>


</body>
</html>
