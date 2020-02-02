class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        wordList = set(wordList) # necessary
        if end not in wordList:
            return 0
        l = [(begin,1)]
        
        while l:
            word,count = l.pop(0)
            if word == end:
                return count
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    temword = word[:i] + j + word[i+1:]
                    if temword in wordList:
                        l.append((temword,count+1))
                        wordList.remove(temword)
        
        return 0