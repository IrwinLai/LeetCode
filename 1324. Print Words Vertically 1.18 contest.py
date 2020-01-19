class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        maxl = max(list(map(len,s)))
        ret = ['' for i in range(maxl)]
        for words in s:
            if len(words) < maxl:
                words += ' '*(maxl-len(words))
            for i in range(maxl):
                ret[i] += words[i]
        for i in range(maxl):
            ret[i] = ret[i].rstrip(" ")
        return ret