class Solution:
    def maxNumberOfFamilies(self, n: int, r: List[List[int]]) -> int:
        if n == 0:
            return 0
        seat = collections.defaultdict(list)
        row = set()
        for i,j in r:
            row.add(i)
        for i in row:
            seat[i] = [0]*10
        for i,j in r:
            seat[i][j-1] = 1
        
        count = 2*(n-len(seat))
        for i in seat:
                if sum(seat[i][1:5]) == 0:
                    count += 1
                    seat[i][1],seat[i][2],seat[i][3],seat[i][4] = 1,1,1,1
                if sum(seat[i][3:7]) == 0:
                    count += 1
                    seat[i][3],seat[i][4],seat[i][5],seat[i][6] = 1,1,1,1
                if sum(seat[i][5:9]) == 0:
                    count += 1
        
        return count