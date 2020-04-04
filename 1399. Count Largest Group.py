class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = collections.defaultdict(list)
        for i in range(1,10):
            d[i] = []
        
        for i in range(1,n+1):
            d[sum(list(map(lambda x:int(x), list(str(i)))))].append(i)
        
        tem = []
        for i in list(d.keys()):
            tem.append(len(d[i]))
        temdict = collections.Counter(tem)
        temdict = sorted(temdict.items(), key = lambda x:-x[0])
        ans = temdict[0][1]
        return ans