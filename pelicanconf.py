#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ilija'
SITENAME = u'Quest for Consciousness'
SITEURL = 'http://127.0.0.1:8000'
SITETITLE = 'Create more time, not money...'
SITEBLURB = 'Time is the ultimate success, not money. <br/>Don\'t use your time to make more money, use your money to make more time.'
SITE_SUMMARY = 'Technological singularity, Quantum computing & Consciousness mapping'
RECENT_MICROBLOG_ARTICLES_NUMBER = 6;
RECENT_NOTEBOOKS_ARTICLES_NUMBER = 4;
DISQUS_SITENAME = "questforconsciousness"
DISQUS_DISPLAY_COUNTS = False
TAGLINE = 'Quest for Consciousness'

PATH = 'content'

STATIC_PATHS = [
    'images',
    'extra/favicon.ico',
    'extra/logo.png'
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.png': {'path': 'logo.png'}
}

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = [
    ('Microblog', '/microblog.html'),
    ('Notebooks', '/notebooks.html'),
    ('Qutips', '/qutips.html'),
    ('More', [
        # ('Singularity', '/pages/singularity.html'),
        # ('Divider', '#'),
        # ('MOOC', '/pages/mooc.html'),
        ('About', '/pages/about.html'),
        ('Terms & Privacy Policy', '/pages/terms-privacy-policy.html')
    ])
]

# Social widget
SOCIAL = (
    # ('Facebook', 'https://www.facebook.com/quest4consc'),
    ('Twitter', 'https://twitter.com/quest4consc'),
    # ('Reddit', 'https://www.reddit.com/user/susumige'),
    ('Github', 'https://github.com/susumige'),
    ('Rss', '/pages/rss-feed.html'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes/simple-notebook'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search', 'sitemap', 'ipynb.markup', 'tag-cloud']

DIRECT_TEMPLATES = ['index', 'search', 'categories']

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

MARKUP = ('md', 'ipynb')

IPYNB_USE_META_SUMMARY = True

CATEGORY_URL = '{slug}.html'
CATEGORY_SAVE_AS = '{slug}.html'

AUTHOR_SAVE_AS = ''

TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_BADGE = True

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

IGNORE_FILES = ['.ipynb_checkpoints']