import time

class Pro1():
    """
    Producer 1 generates numbers.
    """

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, _q):
        time.sleep(3)
