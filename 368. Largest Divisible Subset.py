class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = collections.Counter(s1)
        n = len(s1)
        window = collections.Counter(s2[:n])
        if target == window:
            return True
        for i in range(n,len(s2)):
            window[s2[i-n]] -= 1
            if window[s2[i-n]] == 0:
                window.pop(s2[i-n])
            window[s2[i]] += 1
            if target == window:
                return True
        return False