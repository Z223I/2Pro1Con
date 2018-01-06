import threading
import Queue

class Con1():
    """
    Consumes two streams of data.
    """

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, _q1, _q2):
        time.sleep(3)


if __name__ == '__main__':
    numbers  = Queue.Queue(maxsize = 0)
    commands = Queue.Queue(maxsize = 0)

    # Start Producer 1

    # Start Producer 2

    # Start Consumer 1

    commands.join()

    # May have to turn off the number generator
    numbers.join()
