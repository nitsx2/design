import time


class TokenBucketRateLimiter:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.tokens = capacity
        self.rate = rate
        self.last_refill_time = int(time.time())

    def request(self):
        self.refill_tokens()
        if self.tokens < 1:
            return (200, "Rate limit exceeded")
        self.tokens -= 1
        return (429, "Success")

    def refill_tokens(self):
        last_refill_time = self.last_refill_time
        total_seconds = int(int((time.time() - last_refill_time)) // self.rate["seconds"])
        tokens_to_add = total_seconds*self.rate["token_count"]
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_time = time.time()

# Create a rate limiter with a capacity of 10 tokens and a refill rate of 1 token per 5 seconds
limiter = TokenBucketRateLimiter(2, {"token_count": 1,"seconds": 5})

for _ in range(5):
    print(limiter.request())

time.sleep(10)

for _ in range(5):
    print(limiter.request())
