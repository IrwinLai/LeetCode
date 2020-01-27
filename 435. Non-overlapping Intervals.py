class Solution:
    def eraseOverlapIntervals(self, l: List[List[int]]) -> int:
        if len(l) == 0:
            return 0
        l.sort(key = lambda x:x[1])
        end = l[0][1]
        count = 1
        for i in l[1:]:
            if i[0] >= end:
                end = i[1]
                count += 1
        return len(l) - count