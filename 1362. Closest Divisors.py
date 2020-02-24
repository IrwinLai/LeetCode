class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def helper(n):
            for i in range(int(n**0.5)+1,0,-1):
                if n%i==0:
                    t = abs(i-n//i)
                    a,b = i,int(n//i)
                    break
            return t,a,b
        t1,a1,b1 = helper(num+1)
        t2,a2,b2 = helper(num+2)
        if t1 < t2:
            return [a1,b1]
        else:
            return [a2,b2]