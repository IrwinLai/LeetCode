class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq as hq
        stones=[-i for i in stones]
        hq.heapify(stones)
        for i in range(len(stones)-1):
            a=hq.heappop(stones)
            b=hq.heappop(stones)
            hq.heappush(stones, -abs(a-b))
        return -hq.heappop(stones)