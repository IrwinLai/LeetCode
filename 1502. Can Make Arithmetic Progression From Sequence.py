class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1]-arr[0]
        for i in range(len(arr)):
            if arr[i] != arr[0] + d*i:
                return False
        return True