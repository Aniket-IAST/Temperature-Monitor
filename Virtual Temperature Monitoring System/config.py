NORMAL_MAX = 50
WARNING_MAX = 75
LOG_FILE = "temperature_log.csv"
UPDATE_INTERVAL = 1

import random
import math
class VirtualSensor:
    def __init__(self, mode='random', seed=None):
        self.mode = mode
        self.t = 0
        if seed is not None:
            random.seed(seed)
    def read_raw(self):
        if self.mode == 'random':
            return round(random.uniform(20, 100), 2)
        elif self.mode == 'trend':
            self.t += 1
            return round(60 + 20 * math.sin(self.t * 0.1), 2)
    def read_normalized(self):
        temp = self.read_raw()
        return temp / 100.0