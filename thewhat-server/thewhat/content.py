"""
I am responsible for generating, storing and randomizing theWHATs
"""

from collections import deque


class WHAT(object):

    def __init__(self, queue_size=10):
        self.queue = deque(maxlen=queue_size)
        self._init_queue()

    def _init_queue(self):
        """
        Populate the queue with theWHATs
        """
        for i in range(self.queue.maxlen - len(self.queue)):
            # Iterate for the size of queue, which don't have elements.
            self.push_one()

    def give_one(self):
        """
        Pop one; generate and add one.
        """
        content = self.pop_one()
        self.push_one()
        return content

    def pop_one(self):
        """
        Pop one item from the queue
        """
        return self.queue.popleft()

    def push_one(self):
        """
        Generate and add one theWHAT to the queue
        """
        pass



theWHAT = WHAT()

def give_one():
    return theWHAT.give_one()
