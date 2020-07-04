class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr)%k != 0:
            return False
        
        arr = list(map(lambda x:x%k, arr))
        d = collections.Counter(arr)
        # print(d)
        
        for i in d:
            if d.get(0,0) % 2 != 0:
                return False
            
            if i == k-i:
                if d.get(i,0) % 2 !=0:
                    return False
                
            if i != 0 and i != k-i:
                if (d.get(i,0)+d.get(k-i,0)) % 2 != 0:
                    return False
        return True