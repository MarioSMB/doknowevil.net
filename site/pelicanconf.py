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

THEME_COLOR = 'blue'
SIDEBAR_DISPLAY = ['about', 'categories', 'tags']
SIDEBAR_ABOUT = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi quae hic dicta eius ad quam eligendi minima praesentium voluptatum? Quidem quaerat eaque libero velit impedit dicta, repudiandae sapiente. Deserunt, excepturi."

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
LINKS = (('here','#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
