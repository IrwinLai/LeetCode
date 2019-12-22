class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        d = {}
        for i in range(len(s)-minSize+1):
            if len(set(s[i:i+minSize])) <= maxLetters:
                    d[s[i:i+minSize]] = d.get(s[i:i+minSize],0) + 1
        if len(d) == 0:
            return 0
        return max(d.values())
        
                    