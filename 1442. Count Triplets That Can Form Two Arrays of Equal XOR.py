class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        for i in range(n-1):
            a = arr[i]
            for j in range(i+1,n):
                a ^= arr[j]
                b = arr[j]
                for k in range(j,n):
                    b ^= arr[k]
                    if a == b:
                        count += 1
        return count
                    