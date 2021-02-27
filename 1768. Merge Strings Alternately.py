class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        word1,word2 = list(word1),list(word2)
        n1,n2 = len(word1),len(word2)
        if n1 <= n2:
            for i in range(n1):
                ans.append(word1[i])
                ans.append(word2[i])
            ans.extend(word2[i+1:])
        else:
            for i in range(n2):
                ans.append(word1[i])
                ans.append(word2[i])
            ans.extend(word1[i+1:])
            
        return "".join(ans)
        