class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while(i < j):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                tem1 = s[i:j]
                tem2 = s[i+1:j+1]
                return tem1 == tem1[::-1] or tem2 == tem2[::-1]
        return True
                