class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        remain = 0
        while numBottles:
            ans += numBottles
            remain += numBottles
            numBottles = remain // numExchange
            remain -= numBottles * numExchange
        return ans