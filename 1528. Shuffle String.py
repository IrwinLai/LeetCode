class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ret = ["" for _ in range(len(s))]
        for i in range(len(indices)):
            ret[indices[i]] = s[i]
        return "".join(ret)