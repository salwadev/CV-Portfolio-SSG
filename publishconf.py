#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Vos configurations de production...
SITEURL = ''
RELATIVE_URLS = True

# Désactiver le feed RSS pour un CV
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Optimisations pour la production
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]