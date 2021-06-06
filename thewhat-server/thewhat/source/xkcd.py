"""
Random comics from XKCD

Quota: 5%
"""

from .base import Source

import requests
from lxml import html


class XKCD(Source):

    def __init__(self):
        self.url = "https://c.xkcd.com/random/comic/"

    def quota(self):
        return 0.05

    def get(self):
        page = requests.get(self.url)
        tree = html.fromstring(page.text)
        image_attributes = tree.get_element_by_id("comic").getchildren()[0].attrib
        src = image_attributes["src"]
        if src.startwith("//"):
            src = "https:" + src
        content = image_attributes["title"]
        title = image_attributes["alt"]
        return {
            "type": "image",
            "src": src,
            "content": content,
            "title": title
        }
