class Solution:
    def countOrders(self, n: int) -> int:
        tem = 1
        for i in range(1,n+1):
            tem *= ((2*i*(2*i-1))/2)
            tem %= (10**9+7)
        return int(tem)