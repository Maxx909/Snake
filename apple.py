import random
from constants import CELLX, CELLY

class Apple:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, CELLX - 1)
        self.y = random.randint(0, CELLY - 1)
