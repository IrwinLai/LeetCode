class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if len(rounds) == 1:
            return rounds
        d = [0]*n
        d[rounds[0]-1] = 1
        for i in range(1,len(rounds)):
            if rounds[i] > rounds[i-1]:
                for k in range(rounds[i-1],rounds[i]):
                    d[k] += 1
            else:
                for k in range(rounds[i-1],n):
                    d[k] += 1
                for k in range(0,rounds[i]):
                    d[k] += 1
        
        ret,m = [],-1
        for i in range(len(d)):
            if m < d[i]:
                ret = [i+1]
                m = d[i]
            elif m == d[i]:
                ret.append(i+1)
        return ret