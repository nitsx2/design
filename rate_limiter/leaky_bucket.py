"""The leaky bucket algorithm is another method used for rate limiting, similar to the token bucket algorithm. It controls the rate of incoming data or requests by buffering them in a "bucket" and allowing them to be processed at a steady rate. If the incoming rate exceeds the processing rate, the excess data is discarded or delayed.
Here's a simple explanation of the leaky bucket algorithm:
-Imagine you have a bucket with a small hole at the bottom.
-Incoming data or requests are like water pouring into the bucket.
-The bucket has a maximum capacity, representing the maximum number of data or requests that can be stored.
-The leaky bucket algorithm regulates the flow by allowing data or requests to leak out of the bucket at a steady rate.
-If the incoming flow is too fast and the bucket becomes full, any excess data or requests overflow and are discarded.
"""
import time


class LeakyBucket(object):
    def __init__(self, capacity, reset_rate=60):
        self.queue_capacity = capacity
        self.queue = []
        self.reset_rate = reset_rate # inseconds
        self.last_reset_time = time.time()

    def execute(self):
        self.reset_queue()
        if len(self.queue) < self.queue_capacity:
            self.queue.append(True)
            return True
        else:
            return False

    def reset_queue(self):
        if time.time() - self.last_reset_time > self.reset_rate:
            self.queue = []
            self.last_reset_time = int(time.time())

lb = LeakyBucket(3, 2)

for i in range(5):
    print(lb.execute())

time.sleep(3)

for i in range(5):
    print(lb.execute())