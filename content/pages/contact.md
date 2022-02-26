title: Contact
date: 2021-12-09
category: Main


<link rel="stylesheet" href="/static/theme/css/formspree.css" type="text/css" />

<div class="mx-auto" style="width: 90%;" >
<form class="text-muted" id="fs-frm" name="simple-contact-form" accept-charset="utf-8" action="https://formspree.io/f/xnqwdnle" method="post" >
  <fieldset id="fs-frm-inputs">
    <label for="full-name">Full Name</label>
    <input type="text" name="name" id="full-name" placeholder="First and Last" required="">
    <label for="email-address">Email Address</label>
    <input type="email" name="_replyto" id="email-address" placeholder="email@domain.tld" required="">
    <label for="message">Message</label>
    <textarea rows="5" name="message" id="message" placeholder="Your messege." required=""></textarea>
    <input type="hidden" name="_subject" id="email-subject" value="Contact Form Submission">
  </fieldset>
  <input type="submit" value="Submit">
</form>
</div>

<br>


<script type="text/javascript">
  function codeAddress() {
    document.getElementById("fs-frm").reset();
  }
  window.onload = codeAddress;
  </script>