class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        res = sum(A[:k])
        tem = res
        for i in range(1,k+1):
            tem = tem - A[k-i] + A[-i]
            res = max(res,tem)
        return res