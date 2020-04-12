class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = set()
        for i in words:
            for j in words:
                if i != j and i in j:
                    ret.add(i)
        return list(ret)