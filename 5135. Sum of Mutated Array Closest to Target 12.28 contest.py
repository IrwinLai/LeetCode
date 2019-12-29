class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr = sorted(arr)
        n = len(arr)
        s = 0
        if (target - s) // (n) <= arr[0]:
                return round((target - s) / (n))
        for i in range(len(arr)-1):
            s += arr[i]
            if (target - s) // (n-i-1) <= arr[i+1]:
                return round((target - s) / (n-i-1))