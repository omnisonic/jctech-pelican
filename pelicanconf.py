AUTHOR = 'jctech'
SITENAME = 'jctech'
SITEURL = ''

PATH = 'content'
THEME = 'blue-penguin'
TIMEZONE = 'America/Denver'
DISPLAY_FOOTER = None
STATIC_PATHS = [
    'images',
    'extra',  # this
]
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
}
DEFAULT_LANG = 'en'
# DISPLAY_PAGES_ON_MENU = True
# MENUITEMS = (('About', '/pages/about.html'),
#         ('Contact', '/pages/contact.html'),
#         ('Portfolio', '/pages/portfolio.html'))
# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
PLUGINS = [
    # ...
    'minchin.pelican.plugins.nojekyll',
    # ...
]
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True