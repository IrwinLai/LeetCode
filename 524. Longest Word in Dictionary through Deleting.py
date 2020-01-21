class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def f(word,sen):
            '''
            i,j = 0,0
            while i < len(word) and j < len(sen):
                if word[i] == sen[j]:
                    i += 1
                j += 1
            return i == len(word)
            '''
            sen+='1'
            for i in list(word):
                tem = sen.find(i)
                if tem >= 0:
                    sen = sen[tem+1:]
                else:
                    return False
            return True
            
        if len(s) == 0:
            return ''
        
        d.sort(key = lambda x:(-len(x),x))
        
        for i in d:
            if f(i,s):
                return i
            
        return ''