class Solution:
    def numTeams(self, r: List[int]) -> int:
        n = len(r)
        if n < 3:
            return 0
        
        greater = defaultdict(int)
        smaller = defaultdict(int)
        count = 0
        
        for i in range(n-1):
            for j in range(i+1,n):
                if r[i] > r[j]:
                    greater[i] += 1
                else:
                    smaller[i] += 1
                    
        for i in range(n-2):
            for j in range(i+1,n):
                if r[i] > r[j]:
                    count += greater[j]
                else:
                    count += smaller[j]
                    
        return count