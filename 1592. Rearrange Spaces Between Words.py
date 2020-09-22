class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = text.count(' ')
        tem = text.split(' ')
        t = []
        for i in tem:
            if i != '':
                t.append(i)
        m = len(t)
        if m == 1:
            return str(t[0])+" "*n
        
        space = n//(m-1)*" "
        remain = n%(m-1)*" "
        ans = space.join(t)+remain
        
        return ans