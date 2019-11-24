class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        right = sorted(heights)
        count = [heights[i] != right[i] for i in range(len(heights))]
        
        return sum(count)