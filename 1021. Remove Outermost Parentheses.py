class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        tem = 0
        res = []
        for i in S:
            if tem == 0 and i == '(':
                tem += 1
            elif tem == 1 and i == ')':
                tem -= 1
            elif i == '(':
                tem += 1
                res.append(i)
            else:
                tem -= 1
                res.append(i)
        return ''.join(res)
        
        
        '''
        l = list(S)
        m = [1 if l[i] == '(' else -1 for i in range(len(l))]
        
        t = []
        for i in range(len(m)):
            if sum(m[:i+1]) == 0:
                t.append(i)
        w = m[1:t[0]]
        if len(t) >1:
            for i in range(1,len(t)):
                w.extend(m[t[i-1]+2:t[i]])
        
        r = ['(' if w[i] == 1 else ')' for i in range(len(w))]
        r = ''.join(r)
        return r
        '''