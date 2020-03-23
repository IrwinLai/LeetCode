class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.arr = []

    def push(self, x: int) -> None:
        if len(self.arr) < self.max:
            self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) <= 0:
            return -1
        else:
            tem = self.arr[-1]
            self.arr.pop(len(self.arr)-1)
            return tem

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.arr))):
            self.arr[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)