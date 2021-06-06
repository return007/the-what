from .dontevenreply import DontEvenReply
from .livecam import LiveCam
from .randomwebsite import RandomWebsite
from .xkcd import XKCD

import random


SOURCES = [
    DontEvenReply,
    LiveCam,
    RandomWebsite,
    XKCD,
]


class Mixer:
    """
    Mix all the sources and outputs a single randomized feed
    """

    def __init__(self):
        self.sources = [
            klass() for klass in SOURCES
        ]
        self.prob_distribution = [
            s.quota() for s in self.sources
        ]

    def mix(self):
        obj = random.choices(self.sources, self.prob_distribution, k=1)[0]
        return obj.get()
