class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, start, = {}, 0, 0
        for i in range(len(s)):
            ch = s[i]
            if ch in dic:
                res = max(res, i-start)
                start = max(start, dic[ch]+1)
            dic[ch] = i
        return max(res, len(s)-start)
    
        '''
        s = list(s)
        tem = []
        count = 0
        for i in range(len(s)):
            if s[i] not in tem:
                tem.append(s[i])
            else:
                count = max(count,len(tem))
                tem = tem[tem.index(s[i])+1:]
                tem.append(s[i])
        count = max(count,len(tem))
        return count
        '''