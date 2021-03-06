#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marko Kasikovic'
SITENAME = u'Marko Kasikovic'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

THEME = "/home/marko/pelican-themes/Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('LinkedIn', 'https://www.linkedin.com/in/marko-kasikovic-79761385'),
         ('Github', 'https://github.com/Kasikov'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
