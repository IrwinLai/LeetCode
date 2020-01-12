class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        l = []
        for i in range(len(text)):
            for j in range(i+2,len(text)+1,2):
                t = (j-i)//2
                if text[i:i+t] == text[i+t:j]:
                    l.append(text[i:j])
        return len(set(l))
                