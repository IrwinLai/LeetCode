class Solution:
    def minDays(self, A, m, k):
        if m * k > len(A): return -1
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0
            for a in A:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left

'''
class Solution:
    def minDays(self, bloomDay: List[int], target: int, k: int) -> int:
        days = sorted(list(set(bloomDay)))
        d = collections.Counter(bloomDay)
        for i in range(1,len(days)):
            d[days[i]] += d[days[i-1]]
        
        def helper(t):
            t = days[t]
            if d[t] < k*target:
                -1
                
            tem = ""
            count = 0
            for j in bloomDay:
                if j>t:tem += '0'
                else:tem += '1'

            j = 0
            while j+k <= len(tem):
                if tem[j:j+k] == '1'*k:
                    count += 1
                    j += k
                else:
                    j += 1
            
            return count
        
        l,r = 0,len(days)-1
        while l < r-1:
            m = l + (r-l)//2
            if helper(m) >= target:
                r = m
            else:
                l = m
            

        if helper(l) >= target:
            return days[l]
        if helper(r) >= target:
            return days[r]
        return -1
'''
                    
            
                    