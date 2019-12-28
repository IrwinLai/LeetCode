class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        def sumeven(l):
            s = 0
            for i in l:
                if i%2 == 0:
                    s+=i
            return s
        s = sumeven(A)
        ret = []
        for item in queries:
            tem = A[item[1]]
            A[item[1]] += item[0]
            if tem%2 == 1 and A[item[1]]%2 == 0:
                s += A[item[1]]
            elif tem%2 == 0 and A[item[1]]%2 == 0:
                s = s-tem+A[item[1]]
            elif tem%2 == 0 and A[item[1]]%2 == 1:
                s -= tem
            ret.append(s)
        return ret