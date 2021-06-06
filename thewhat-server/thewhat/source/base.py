"""
Defines Generic source.
"""

class Source(object):
    """
    A generic source class
    """

    def quota(self):
        """
        What quota (percentage) should be it made available to the user.
        """
        raise NotImplementedError

    def get(self):
        """
        Logic to actually fetch the contents and return a proper response to be
        directly consumed by the theWHAT application

        :return:
          `dict` containing the following items:
            - "type"
            - "src"
            - "content"
            - "title"
        """
        raise NotImplementedError
