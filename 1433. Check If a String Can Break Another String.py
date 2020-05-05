class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(list(s1)))
        s2 = "".join(sorted(list(s2)))

        s3 = s2[::-1]
        n = len(s1)
        for i in range(n):
            if ord(s1[i]) < ord(s2[i]):
                break
            if i == n-1:
                return True
            
        for i in range(len(s1)):
            if ord(s1[i]) > ord(s2[i]):
                break
            if i == n-1:
                return True
        
        for i in range(n):
            if ord(s1[i]) < ord(s3[i]):
                break
            if i == n-1:
                return True
            
        for i in range(n):
            if ord(s1[i]) > ord(s3[i]):
                break
            if i == n-1:
                return True
            
        return False