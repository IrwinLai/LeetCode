class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        sL,sR,eL,eR = 0,0,0,0
        for i in range(len(start)):
            if start[i] == 'L':
                sL += 1
            if start[i] == 'R':
                sR += 1   
            if end[i] == 'L':
                eL += 1   
            if end[i] == 'R':
                eR += 1
            if sL > eL or sR < eR:
                return False
        
        return sL == eL and sR == eR and sL+sR <= len(start)/2