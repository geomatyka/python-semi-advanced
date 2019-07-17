from time import time, ctime, localtime


class Order:
    def __init__(self, name):
        self.name = name
        self.placing_h = time()
        self.completion_h = None
        self.pickup_h = 0

    def __str__(self):
        return f'{self.name} {ctime(self.placing_h)} {(self.completion_h - self.placing_h):.0f}s {(self.pickup_h - self.completion_h):.0f}s'
