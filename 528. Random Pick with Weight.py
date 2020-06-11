class Solution:
    def __init__(self, w: List[int]):
        self.nums = [w[0]]
        for i in range(1, len(w)):
            self.nums.append(self.nums[-1] + w[i])
        

    def pickIndex(self) -> int:
        val = random.randrange(1, self.nums[-1] + 1)
        return bisect_left(self.nums,val)