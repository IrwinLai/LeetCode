class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        if left:
            for i in left:
                ans = max(ans,i)
        if right:
            for j in right:
                ans = max(ans,n-j)
        return ans