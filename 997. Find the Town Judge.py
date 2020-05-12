class Solution:
    def findJudge(self, N: int, A: List[List[int]]) -> int:
        c = [[] for i in range(N)]
        trustother = set()
        for x,y in A:
            c[y-1].append(x-1)
            trustother.add(x-1)
            
        for i in range(N):
            if len(c[i]) == N-1 and i not in trustother:
                return i+1

        return -1