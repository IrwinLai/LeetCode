class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        n = len(searchWord)
        for i in range(len(sentence)):
            if len(sentence[i]) >= len(searchWord):
                if sentence[i][:n] == searchWord:
                    return i+1
        return -1