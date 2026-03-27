class BrowserHistory:

    class Node:
        def __init__(self, url):
            self.url = url
            self.prev = None
            self.next = None


    def __init__(self, homepage: str):
        self.curr = BrowserHistory.Node(homepage)

    def visit(self, url: str) -> None:
        new = BrowserHistory.Node(url)
        new.prev = self.curr
        self.curr.next = new
        self.curr = new

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev is not None:
            self.curr =  self.curr.prev
            steps -= 1
        return self.curr.url
    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next is not None:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)