class RecentCounter(object):

    def __init__(self):
        self.counter = []

    def ping(self, t):
        while self.counter and t - self.counter[0] > 3000:
            self.counter.pop(0) ##deque
        self.counter.append(t)
        return len(self.counter)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)