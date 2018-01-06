import time
import threading

class Pro1():
    """
    Producer 1 generates numbers.
    """

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, _q):
        while True:
            name = threading.currentThread().getName()
            print "Producer thread:  ", name
            item = 'item-1'
            _q.put(item)
            print item
            time.sleep(4)
