title: Set a Home Page in Pelican Site Generator instead of a Blog.
Date: 2021-02-25
Category: Pelican
Author: John Clarke

---

Pelican is a website generator using python.
The default configuration is to generate the website as a blog.  Blogs use a "blogroll" where summaries of each blog are shown on the page as you scroll down.  This is usually set up on the blog website index.  This is how thing are set up in Pelican by default.  But what if you want to make a landing page or some other kind of content for you the home page of your website?  This can be done with Pelican with some configurations.

The details of how to do this can be found in the official Documentations https://docs.getpelican.com/en/latest/

The part of the documentation that specifically addresses this is in the FAQ: https://docs.getpelican.com/en/latest/faq.html#how-can-i-use-a-static-page-as-my-home-page

Here is a screen shot:

<img src="/images/page-as-home-pelican.jpg" class="img-fluid">

The Pelican "meta data" for every page or post should have "title: " .
To make the it a post rather then a page we simply include  the date to the meta data.
So for a "home" page we will leave out the date.  To make the page a "home" page we will include:

<pre class="bg-dark"><code>
    title:  Home
    URL:
    save_as: index.html

</code></pre>


This bypasses generating the blog roll on the index.html and instead generates our "home" page there.

If we still want to include blog on our website we need to modify our "pelicanconf.py" file to include: 

<pre class="bg-dark"><code>

    INDEX_SAVE_AS = 'blog_index.html'

</code></pre>


The "index.html" template within Pelican themes is used to set up the blog by default.  The above setting in the pelicanconf.py tells pelican to generate that blog on the "blog_index.html" in our output.  

As a side note, another important distinction between posts and pages, is that pages need to be inside the pages director eg /content/pages/; whereas the md files directly under the /content/ are treated as post and included in the blog roll index.  

So The static home page should be in the /content/pages/ directory.


To get our blog to show up in the menu we can the following to our pelicanconf.py: 

<pre class="bg-dark"><code>

    MENUITEMS = ('Blog', '/blog_index.html'),

</code></pre>
