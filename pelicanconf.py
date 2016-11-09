#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'mingz'  # 默认作者
SITENAME = u"mingz's home"
SITEURL = 'http://localhost'
TIMEZONE = 'Europe/Paris'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

PATH = 'content'

THEME = "themes/mycustomtheme"  # 主题
GITHUB_URL = 'http://github.com/mingz2013/'
DISQUS_SITENAME = "mingz's home"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 10  # 分页长度
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

USE_FOLDER_AS_CATEGORY = True

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
          ('lastfm', 'http://lastfm.com/user/akounet'),
          ('github', 'http://github.com/ametaireau'),)

# global metadata to all the contents
DEFAULT_METADATA = {'yeah': 'it is'}

# static paths will be copied under the same name
# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "pdfs",
    'extra/robots.txt',
    'extra/CNAME'
]

# custom page generated with a jinja2 template
# TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
