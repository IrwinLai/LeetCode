class Solution:
    def validateBinaryTreeNodes(self, n: int, l: List[int], r: List[int]) -> bool:
        p = list((zip(l,r)))
        count = 1
        for x,y in p:
            if x >= 0:
                count += 1
            if y >= 0:
                count += 1
            count -= 1
            if count < 0:
                return False
        return count == 0