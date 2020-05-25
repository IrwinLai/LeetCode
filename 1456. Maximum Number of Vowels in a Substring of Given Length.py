class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = ['a','e','i','o','u']
        s1 = []
        for i in s:
            if i in l:
                s1.append(1)
            else:
                s1.append(0)
        tem = sum(s1[0:k])
        ans = tem
        for i in range(len(s1)-k):
            tem = tem-s1[i]+s1[i+k]
            ans = max(tem,ans)
        return ans
            