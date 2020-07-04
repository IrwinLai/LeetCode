class Solution:
    def isPathCrossing(self, path: str) -> bool:
        path = list(path)
        tem = set()
        tem.add((0,0))
        cur = [0,0]
        
        for i in path:
            if i == 'N':
                cur[1] += 1
            if i == 'S':
                cur[1] -= 1
            if i == 'W':
                cur[0] -= 1
            if i == 'E':
                cur[0] += 1
        
            if (cur[0],cur[1]) in tem:
                return True
            tem.add((cur[0],cur[1]))

        return False