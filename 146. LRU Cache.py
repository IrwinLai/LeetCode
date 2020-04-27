class LRUCache:

    def __init__(self, capacity: int):
        self.d = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            tem = self.d.pop(key)
            self.d[key] = tem
            return tem
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.d.popitem(last = False)
        self.d[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)