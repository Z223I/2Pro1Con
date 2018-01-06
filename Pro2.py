class Pro2():
    """
    Producer 2 generates commands.
    """

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, _q):
        time.sleep(3)
