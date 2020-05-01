class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)
        res = sorted(d,key = lambda x:[-d[x],x])
        return res[:k]