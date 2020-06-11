class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res,stack = [0]*len(T),[]
        for i,t in enumerate(T):
            # record all the new higner t
            while stack and stack[-1][1] < t:
                cur = stack.pop()[0]
                res[cur] = i - cur
            stack.append((i,t))
        return res
        
        
        '''  # TLE
        res = []
        for i in range(len(T)):
            count,flag = 0,0
            for j in range(i,len(T)):
                if T[j] > T[i]:
                    flag = 1
                    break
                count += 1
            if flag == 0:
                res.append(0)
            else:
                res.append(count)
        return res
        '''