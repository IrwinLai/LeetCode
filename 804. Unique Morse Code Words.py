class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        mcode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = []
        for i in words:
            tem = []
            for j in range(len(i)):
                tem.append(mcode[ord(i[j])-97])
            res.append("".join(tem))
        
        # print(res)
        return len(set(res))