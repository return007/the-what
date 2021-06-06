"""
Random images from Tumblr (https://tumblr.com)

Quota: 5%
"""

from .base import Source

import requests
from lxml import html


class Tumblr(Source):

    def quota(self):
        return 0.05

    def get(self):
        pass
