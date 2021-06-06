"""
Random article from Wikipedia (https://wikipedia.org)

TODO: Add some famous lists like:

 - https://en.wikipedia.org/wiki/List_of_conspiracy_theories

Quota: 1%
"""

from .base import Source

import requests


class Wikipedia(Source):

    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/Special:Random"

    def quota(self):
        return 0.01

    def get(self):
        resp = requests.get(self.url, allow_redirects=False)
        src = resp.headers["Location"]
        return {
            "type": "website",
            "src": src,
            "content": "",
            "title": "Wikipedia article"
        }
