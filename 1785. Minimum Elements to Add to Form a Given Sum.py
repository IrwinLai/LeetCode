class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        ans = abs(goal - sum(nums))
        if ans % limit == 0:
            ans = ans // limit
        else:
            ans = ans // limit + 1
        return ans