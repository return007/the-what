"""
Random memes from KnowYourMeme (https://knowyourmeme.com)

Quota: 5%
"""

from .base import Source

import requests
from lxml import html


class KnowYourMeme(Source):

    def quota(self):
        return 0.05

    def get(self):
        pass
