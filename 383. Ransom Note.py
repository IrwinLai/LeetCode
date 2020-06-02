class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = collections.Counter(magazine)
        for i in ransomNote:
            if d.get(i,0) == 0:
                return False
            else:
                d[i] -= 1
        return True