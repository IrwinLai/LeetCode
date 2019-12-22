class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def selfdividing(n):
            if n < 10:
                return True
            else:
                s = str(n)
                if '0' in s:
                    return False
                else:
                    for i in s:
                        if n % int(i) != 0:
                            return False
                return True
        
        ret = []
        for i in range(left,right+1):
            if selfdividing(i) == True:
                ret.append(i)
                
        return ret
    
        '''
        def selfdividing(n):
            if n < 10:
                return True
            else:
                d = collections.Counter(str(n))
                for i in d.keys():
                    if i == '0' or n % int(i) != 0:
                        return False
                return True
        '''