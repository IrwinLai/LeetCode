class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd = 0
        for chip in chips:
            odd += chip % 2
        return min(len(chips) - odd,odd)
        
        '''
        cost = 10**9
        s = list(set(chips))
        for i in s:
            count = 0
            for chip in chips:
                count += abs(chip-i) % 2
            cost = min(cost,count)
        return cost
        '''