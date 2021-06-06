"""
Random images from YouTube (https://youtube.com)

Quota: 20%
"""

from .base import Source

import requests
from lxml import html


class YouTube(Source):

    def quota(self):
        return 0.25

    def get(self):
        pass
