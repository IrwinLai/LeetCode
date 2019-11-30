class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        import collections
        d = collections.Counter(chars)
        count = 0
        for item in words:
            tem = collections.Counter(item)
            flag = 0
            for i in tem.keys():
                if tem[i] > d.get(i,0):
                    flag = 1
                    break
            if flag == 0:
                count += len(item)
        return count
        
        #return sum([len(word) for word in words if all(0 < word.count(x) <= chars.count(x) for x in word)])