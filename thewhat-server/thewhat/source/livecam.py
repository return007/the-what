"""
Livecams from https://explore.org/livecams

Quota: 1%
"""

from .base import Source

import requests
from random import randrange


class LiveCam(Source):

    def __init__(self):
        self.url = "https://d11gsgd2hj8qxd.cloudfront.net/streams.json"
        self.tmpl = "https://youtube.com/embed/%s"

    def quota(self):
        return 0.01

    def get(self):
        links = []
        try:
            r = requests.get(self.url)
        except requests.exceptions.HTTPError:
            return
        contents = r.json()
        streams = contents["streams"]
        for s in streams:
            video_meta = s["youtubeLiveEvents"]
            links.append(video_meta[0]["youtubeId"])

        idx = randrange(len(links))
        choice = self.tmpl % links[idx]
        return {
            "type": "video",
            "src": choice,
            "content": "",
            "title": streams[idx]["name"]
        }
