import time

class Stopwatch:
    def __init__(self):
        self.first = None
        self.end = None
        self.time_calc = None

    def start(self):
        self.first = time.time()

    def stop(self):
        self.end = time.time()
        self.time_calc_micro = (self.end - self.first) * ( 10 ** 6 )
