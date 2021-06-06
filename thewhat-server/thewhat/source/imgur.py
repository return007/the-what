"""
Random images from Imgur (https://imgur.com)

Quota: 5%
"""

from .base import Source

import requests
from lxml import html


class Imgur(Source):

    def quota(self):
        return 0.05

    def get(self):
        pass
