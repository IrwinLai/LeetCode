class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        U = L = 0
        for i in moves:
            if i == "U":
                U += 1
            elif i == 'D':
                U -= 1
            elif i == 'L':
                L += 1
            elif i == 'R':
                L -= 1
        
        return (U==0 and L==0)