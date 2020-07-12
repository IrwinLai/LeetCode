class Solution:
    def getMinDistSum(self, p: List[List[int]]) -> float:
        x,y,n = 0,0,len(p)
        for a,b in p:
            x += a
            y += b
        x,y = x/n,y/n
        e = 10 ** (-8)
        
        while 1:
            sum1,sum2,sum3 = 0,0,0
            for a,b in p:
                dis = ((x-a)**2 + (y-b)**2)**0.5
                if dis == 0:
                    dis = e
                sum1 += a/dis
                sum2 += b/dis
                sum3 += 1/dis
            px,py = x,y
            x = sum1 / sum3
            y = sum2 / sum3
            if abs(x-px) < e and abs(y-py) < e:
                break
        
        ans = 0
        for a,b in p:
            ans += ((px-a)**2 + (py-b)**2)**0.5
        
        return ans