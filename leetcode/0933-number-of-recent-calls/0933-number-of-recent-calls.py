class RecentCounter:

    def __init__(self):
        self.request_queue = deque()
        

    def ping(self, t: int) -> int:
        self.request_queue.append(t)
        while self.request_queue[0] < t - 3000:
            self.request_queue.popleft()
        return len(self.request_queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)