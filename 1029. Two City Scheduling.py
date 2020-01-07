class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0] - x[1])
        ret = 0
        n = len(costs)
        for i in range(n):
            if i < n//2:
                ret+=costs[i][0]
            else:
                ret+=costs[i][1]
        return ret