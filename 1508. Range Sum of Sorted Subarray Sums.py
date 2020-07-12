class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub = []
        for i in range(n):
            tem = nums[i]
            sub.append(tem)
            for j in range(i+1,n):
                tem += nums[j]
                sub.append(tem)
        sub.sort()

        return sum(sub[left-1:right])