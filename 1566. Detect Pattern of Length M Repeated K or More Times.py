class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for j in range(len(arr)-m):
            count = 1
            for i in range(j+m,len(arr),m):
                if arr[i:i+m] != arr[i-m:i]:
                    count = 1
                else:
                    count += 1
                if count >= k:
                    return True
        return False