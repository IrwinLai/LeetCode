from functools import lru_cache
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        # have to record index, ow TLE
        d = {}
        for i in range(n):
            if arr[i] in d:
                d[arr[i]].append(i)
            else:
                d[arr[i]] = [i]
                
        s1 = set()
        s2 = set()
        level = set()
        level.add(0)
        count = -1
        while level:
            tem = set()
            count += 1
            for i in level:
                if i == n-1:
                    return count
                
                
                if i-1 >= 0 and i-1 not in s1:
                        tem.add(i-1)
                if i+1 < n and i+1 not in s1:
                        tem.add(i+1)
                        
                if arr[i] not in s2:
                    for j in d[arr[i]]:
                        if i != j and j not in s1:
                            tem.add(j)
                            
                s1.add(i)
                s2.add(arr[i])
                
            level = tem
        return count