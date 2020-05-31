class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        mod = 10**9 + 7
        hc.sort()
        vc.sort()
        hc2,vc2 = [hc[0]],[vc[0]]
        if len(hc) > 1:
            for i in range(1,len(hc)):
                hc2.append(hc[i]-hc[i-1])
        hc2.append(h-hc[-1])
        if len(vc) > 1:
            for i in range(1,len(vc)):
                vc2.append(vc[i]-vc[i-1])
        vc2.append(w-vc[-1])
        
        return (max(hc2)*max(vc2))%mod