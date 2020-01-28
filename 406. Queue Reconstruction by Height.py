class Solution:
    def reconstructQueue(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) == 1:
            return A
        A.sort(key = lambda x:(-x[0],x[1]))
        ret = []
        for i in A:
            ret.insert(i[1],i)
        return ret