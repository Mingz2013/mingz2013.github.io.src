#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'mingz'  # 默认作者
DATE_FORMATS = {}  # 日期格式设置
USE_FOLDER_AS_CATEGORY = True  # 用目录作为类别
DEFAULT_CATEGORY = 'misc'  # 默认文章分类
DEFAULT_DATE_FORMAT = '%a %d %B %Y'  # 默认日期格式
DISPLAY_PAGES_ON_MENU = True  # 是否在模板菜单上显示页面
DISPLAY_CATEGORIES_ON_MENU = True  # 是否在模板菜单上显示分类
DEFAULT_DATE = "fs"  # (2012, 3, 2, 14, 1, 1) 默认日期
# global metadata to all the contents
DEFAULT_METADATA = {'yeah': 'it is'}  # 文章和页面的默认元数据设置
# FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2}).*'
DELETE_OUTPUT_DIRECTORY = False  # 删除putput目录，优点在于避免生成不必要的文件，同时， 该设置具有一定风险，请谨慎处理。
JINJA_EXTENSIONS = []  # 使用Jinja扩展列表
JINJA_FILTERS = {}  # Jinja2 filters自定义列表

OUTPUT_PATH = 'output/'  # 文件生成目录
PATH = 'content'  # 输入文件目录
PAGE_DIR = 'pages'  # 页面生成目录
ARTICLE_DIR = 'articles'  # 文章输入文件目录
# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False  # 定义是否使用文档相对URL链接，只有当测试时设置为 True
PLUGINS = []  # 插件

SITENAME = u"mingz's home"  # 站点名称
SITEURL = 'http://localhost'  # 站点url

# custom page generated with a jinja2 template
# TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'} # 包含文章生成时的模板页

# static paths will be copied under the same name
# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "pdfs",
    'extra/robots.txt',
    'extra/CNAME'
]  # 在output目录中提供可访问的静态路径 “static”.

TIMEZONE = 'Europe/Paris'

TYPOGRIFY = True  # 如果设置为True, 一些排版效果将会纳入生成的HTML文件中，通过 Typogrify 库, 安装方式: pip install typogrify

DIRECT_TEMPLATES = ('index', 'tags', 'categories',
                    'archives')  # 直接使用模板。 通常情况下直接使用模板生成index页面的内容，(e.g., tags and category index pages). 如果无需标签和分类合集,设置 DIRECT_TEMPLATES = ('index', 'archives')
PAGINATED_DIRECT_TEMPLATES = ('index',)  # 提供可以分页的模板
SUMMARY_MAX_LENGTH = 50  # 文章摘要最大字数。

THEME = "themes/mycustomtheme"  # 主题
GITHUB_URL = 'http://github.com/mingz2013/'
DISQUS_SITENAME = "mingz's home"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 10  # 分页长度

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

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

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
