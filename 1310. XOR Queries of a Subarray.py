class Solution:
    def xorQueries(self, arr1: List[int], arr2: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(arr1) - 1):
            arr1[i + 1] ^= arr1[i]
        for i, j in arr2:
            if i == 0:
                ans.append(arr1[j])
            else:
                ans.append(arr1[i-1]^arr1[j])
        return ans