class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        if k > n:
            return 0
        
        sm = k*threshold
        pre = [0]
        for i in arr:
            pre.append(i+pre[-1])
        
        ans = 0
        for i in range(len(pre)-k):
            if pre[i+k] - pre[i] >= sm:
                ans += 1
            
        return ans
            