class Solution:
    def processQueries(self, q: List[int], m: int) -> List[int]:
        ret = []
        l = [i for i in range(1,m+1)]
        for i in q:
            index = l.index(i)
            ret.append(index)
            l = [l[index]]+l[:index]+l[index+1:]
        return ret
        