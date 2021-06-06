"""
Define Generic source
"""

class Source(object):

    def quota(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError
