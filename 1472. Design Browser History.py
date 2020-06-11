class BrowserHistory:
    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.index += 1
        self.arr = self.arr[:self.index] + [url]

    def back(self, steps: int) -> str:
        self.index = max(self.index-steps, 0)
        return self.arr[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(self.index+steps, len(self.arr)-1)
        return self.arr[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)