"""
Random memes from KnowYourMeme (https://knowyourmeme.com)

Quota: 8%
"""

from .base import Source

import requests
from lxml import html


class KnowYourMeme(Source):

    def quota(self):
        return 0.08

    def get(self):
        pass


def _extract_top_meme_links(pageno=1):
    url = "https://knowyourmeme.com/memes/popular/page/%d" % pageno
    try:
        page = requests.get(url, headers={
            "User-Agent": "theWHAT",
            "Host": "knowyourmeme.com",
        })
    except:
        return []
    etree = html.fromstring(page.text)
    etree.make_links_absolute("https://knowyourmeme.com")
    tbody = etree.find_class("entry-grid-body")[0]
    td = tbody.xpath("tr/td[@class]")
    links = []
    for _td in td:
        links.append(_td.getchildren()[0].attrib["href"])

    return links


def populate_db():
    import time
    links = []
    for i in range(1, 100):
        time.sleep(1)
        links.extend(_extract_top_meme_links(i))
    return links
