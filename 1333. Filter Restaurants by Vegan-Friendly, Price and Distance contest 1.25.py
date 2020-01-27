class Solution:
    def filterRestaurants(self, A: List[List[int]], v: int, p: int, d: int) -> List[int]:
        l = []
        if v == 0:
            for i in A:
                if i[3] <= p and i[4] <= d:
                    l.append(i)
        else:
            for i in A:
                if i[3] <= p and i[4] <= d and i[2] == 1:
                    l.append(i)
        
        l.sort(key = lambda x:(-x[1],-x[0]))
        return [i[0] for i in l]