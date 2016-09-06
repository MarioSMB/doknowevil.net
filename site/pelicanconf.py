#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from functools import partial
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order

AUTHOR = 'Tyler Mulligan'
SITENAME = 'Do Know Evil'
SITEURL = ''

THEME = 'pelican-materialize-blog'

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))
PLUGIN_PATHS = ["plugins", "/home/z/dev/pelican-plugins/"]
PLUGINS = ["liquid_tags", "sitemap", "tipue_search"]

ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}.html'
ARTICLE_URL = 'articles/{date:%Y}/{slug}.html'

TIPUE_SEARCH = True

DEFAULT_DATE_FORMAT = '%b %d, %Y %I:%M %p'

PATH = 'content'

STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'America/Cancun'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('here', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
