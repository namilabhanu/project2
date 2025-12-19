import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity              # max tokens
        self.refill_rate = refill_rate        # tokens per second
        self.tokens = capacity
        self.last_refill = time.time()

    def allow(self):
        now = time.time()

        # Refill tokens based on elapsed time
        elapsed = now - self.last_refill
        self.tokens = min(
            self.capacity,
            self.tokens + elapsed * self.refill_rate
        )
        self.last_refill = now

        # Check if at least 1 token is available
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

bucket = TokenBucket(capacity=5, refill_rate=1)

for i in range(10):
    if bucket.allow():
        print(f"{time.time():.2f} - allowed {i}")
    else:
        print(f"{time.time():.2f} - rate limited {i}")

    time.sleep(0.3)