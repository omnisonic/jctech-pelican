title: Self Hosted comments with Commento and Heroku.
date: 2022-03-03
Category: WebDev
Author: John Clarke

###Comments on your blog or website

Basic Overview 

1. Sign up for free plan with Heroku
2. Click the deploy link in the github repo for commento++
3. Configure your app in Heroku
4. Configure website url in Commento Dashboard
5. Embed script in your website
6. Edit css 

If your looking for a commenting system on your website, and you don't want the unnecessary tracking and bloat of Disqus or facebook comments, then Commento might be a good option for you.



###Commento
<img src="images/commento-heroku-deploy.jpg" class="img-fluid" width="50%">

Commento is privacy focused, lean and does not track or share personal data.  You can either use their hosted plan or you can self-host on your own server or cloud platform.  We are going to use self-hosted.

###Heroku
<img src="images/heroku-screenshot.jpg" class="img-fluid" width="50%">

A good way to try out Commento as a self hosted option is to used Heroku as your cloud application host.

###1. Sign up for free plan with Heroku

Sign-up for a Free account at Heroku.

Heroku has a free plan to get you started with your MVP's or personal projects apps.  The free plan comes with 550 to 1000 dyno hours per month.  Dynos are virtualized Linux containers that run your app and are able to scale to your needs. <a href="https://www.heroku.com/dynos">https://www.heroku.com/dynos</a>

### 2. Click the deploy link in the github repo for commento++


Its a good idea to read  through the readme file of this repo before clicking  the deploy link.

The Github Repo for Commentoplusplus:

 <a href="https://github.com/souramoo/commentoplusplus">https://github.com/souramoo/commentoplusplus</a>
 
This is a fork of Commento that offers additional features and fixes as well as one-click deploy to Heroku. 

Click the deploy link in the github repo for commento++

###3.  Configure your app in Heroku

Sign in if you need to.  Heroku will bring you to the configuration page for deploying Commento

There are just a couple of field that are required.

<img src="/images/create-app-heroku.jpg" class="img-fluid" width="50%">

-App Name 

-COMMENTO_FORBID_NEW_OWNERS 
    default  is false.  You should set this to 'true' so that only you can register an admin account. You can also configure change this later from the heroku dashbar.

-COMMENTO_ORIGIN
    This one is important.  This is the url of where Commento will be hosted.  It will also be where you will login in to your admin dashboard for managing the commenting system.  You can configure a subdomain with your domain host like 'commento.yoursite.com'  or you can just do with the domain that Heroku gives you.  But since you havent created the app yet ,  you don't have the Heroku address for the app yet.  So just put in a place holder like "commento.yoursite.com".  It is important to change this once you get the Heroku address for the app.

All the other setting you can leave as is or change them if you know what your doing.
When you done click on "Deploy app"

It will take a few minute to build and then Heroku will take you to your dashboard where you can see the app.  Heroku will give the app a random name.  You can change this name if you wish to help remember what it is.  


To change your app name click the app and go to settings. In the app name field give your app a new name and then click save. 


When you change the App Name under settings , Heroku will also update its url for the app.

If you plan to use Heroku's url for your app, you need to change it from the place holder used at the beginning.

From the Heroku dashboard, Click on the app and then click on settings.  

Scroll down and look under the config Vars for 'COMMENTO'

On the top right of the screen you can click open app to go to your app url.  When you do, copy the url and come back to your app settings in Heroku to update your COMMENTO_ORIGIN under 'congif vars.'  

Edit this value with pencil icon and paste in your url for your app. click save changes.

### 4. Configure website url in Commento Dashboard

Now its time to set up your Commento dashboard.  You will need to add the website domain where you will be adding the commento scripts.  This is because Commento prevents other websites from embedding your script.  If you don't remember what you app url is you can you can get to it through the Heroku dashboard by clicking on 'open app'.  This brings you to your app url.  Once you login to your app you can see the Commento dashboard.

Click on  '+ New Domain to add your website domains where you will be embedding the commento script. This window pops open:

<img src="/images/commento-add-domain.jpg" class="img-fluid" width="50%">

To get things working I had to add both the wild card:

    %.YOUR-URL.com

and the root domain:

    YOUR-URL.com


###5. Add Commento script to your website

Here is a link to Commento documentation dealing with front end: 

<a href="https://docs.commento.io/configuration/frontend/">https://docs.commento.io/configuration/frontend</a>


We will use the Pelican website generator for this example.  We want to have commenting on the bottom of every post in our blog.  To make this happen in pelican we need to put our Commento script near the bottom of our "article.html" template.  It should look something like this.

    <script defer src="YOUR-APP-NAME.herokuapp.com/js/commento.js"
    data-css-override="{{SITEURL}}/theme/css/commento.css"
    data-auto-init="true">
    </script>
    <div id="commento"></div>
    </div>
    </section>
    {% endblock %}

Make sure you change the 'YOUR-APP-NAME.herokuapp.com'  to the url of your commento app.


###6. Edit CSS

In the above code I have also added 

    data-css-override="{{SITEURL}}/theme/css/commento.css"
    data-auto-init="true"

This tells commento to allow style over-ride and where my css file is.  'commento.css' is a file I created to contain my custom commento styles.  You can see that the comment section below is styled to match the colors of this website.

I used Firefox web-developer tools and inspector to identify and modify the styles to match.  I modified the the styles in Firefox css inspector then copied them over to my 'commento.css'

Please leave a comment below!

---