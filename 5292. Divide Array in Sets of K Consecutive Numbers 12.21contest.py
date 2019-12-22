class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        d = collections.Counter(nums)
        
        while(len(d.keys()) > 0):
            l =sorted(list(d.keys()))
            if len(l) < k:
                return False
            count = 1
            for i in range(k-1):
                count *= (l[i+1] - l[i])
                d[l[i]] -= 1
            d[l[k-1]] -= 1
            if count != 1:
                return False
            for i in l:
                if d[i] == 0:
                    d.pop(i)
        return True