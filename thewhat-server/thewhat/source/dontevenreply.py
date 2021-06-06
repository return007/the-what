"""
Classic super rude emails from DontEvenReply (http://dontevenreply.com)

Quota: 1%
"""

from .base import Source

import requests
from random import randrange


class DontEvenReply(Source):

    def __init__(self):
        self.url = "http://dontevenreply.com/view.php?post=%s"
        self.valid_posts = (2, 113)

    def quota(self):
        return 0.01

    def get(self):
        # Generate a random choice from the valid set of posts
        choice = randrange(*self.valid_posts)
        url = self.url % choice
        return {
            "type": "website",
            "src": url,
            "content": "",
            "title": ""
        }
