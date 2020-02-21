class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        n = len(d)
        res = []
        if n == 0:
            return res
        
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        def dfs(path,index):
            if len(path) == n:
                res.append(path)
            for i in range(index,n):
                for j in list(dic[d[i]]):
                    dfs(path+j,i+1)
        
        dfs("",0)
        return res