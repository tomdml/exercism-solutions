from string import ascii_uppercase as upper, digits
import random
import time


class Robot:
    def __init__(self):
        self.name = ''.join(random.choice(upper) for _ in range(2)) +\
                    ''.join(random.choice(digits) for _ in range(3))

    def reset(self):
        random.seed(id(time.time))
        return self.__init__()
