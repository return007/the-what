"""
Generate random content from https://reddit.com.

Reddit is a great source for random content.

Quota: 20% Scrap + 15% Top posts and comments
"""

from .base import Source

class Reddit(Source):

    def quota(self):
        return 0.15

    def get(self):
        pass


class RedditScrap(Source):

    def quota(self):
        return 0.20

    def get(self):
        pass
