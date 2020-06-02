class Solution:
    def checkIfPrerequisite(self, n: int, p: List[List[int]], q: List[List[int]]) -> List[bool]:
        # Floyd Algorithm
        connected = [[False]*n for _ in range(n)]
        for i,j in p:
            connected[i][j] = True
           
        # k must be out side!
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])
        return [connected[i][j] for i,j in q]