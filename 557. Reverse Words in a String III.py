class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        ret = []
        for item in s:
            ret.append(item[::-1])
        return " ".join(ret)