class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        if len(initialBoxes) == 0:
            return 0
        candy = 0
        key = []
        box = []
        box.extend(initialBoxes)
        while(len(box) != 0):
            count = 0
            for i in box:
                if status[i] == 1:
                    count += 1
                    box.remove(i)
                    candy += candies[i]
                    for j in keys[i]:
                        status[j] = 1
                    box.extend(containedBoxes[i])
            if count == 0:
                return candy
        return candy