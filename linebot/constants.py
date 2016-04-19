# -*- coding: utf-8 -*-

from urlparse import urlparse, urljoin

API_URL_BASE = 'https://trialbot-api.line.me'
__parsed_base_url = urlparse(API_URL_BASE)
API_VERSION = 'v1'
API_URL_EVENTS = urljoin(__parsed_base_url.geturl(), '{}/{}'.format(API_VERSION, 'events'))
