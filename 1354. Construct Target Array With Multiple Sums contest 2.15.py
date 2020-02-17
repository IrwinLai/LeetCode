class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        aim = [1] * n
        if aim == target:
            return True
        
        def helper(l):
            m = 0
            s = 0
            index = 0
            for i in range(n):
                s += l[i]
                if l[i] > m:
                    m = l[i]
                    index = i
            return index, m-(s-m)
            
        while target:
            i,j = helper(target)
            if target[i] <= 1 or j < 1:
                return False
            target[i] = j
            if j == 1:
                if target == aim:
                    return True
            #print(target)