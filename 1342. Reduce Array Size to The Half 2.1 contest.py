class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = 0
        tem = sorted(collections.Counter(arr).values(),reverse = True)
        for i,c in enumerate(tem):
            count += c
            if count >= (len(arr)+1)//2:
                return i+1
            
        '''
        n = len(arr)
        d = collections.Counter(arr)
        l = list(d.keys())
        l.sort(key = lambda x:-d[x])
        count = 0
        tem = 0
        for i in list(l):
            tem += d[i]
            count += 1
            if tem >= (n+1)//2:
                return count
        '''