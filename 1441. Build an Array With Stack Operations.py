class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        ret = []
        for i in range(1,n+1):
            if i in target:
                ret.append('Push')
                ans.append(i)
            if i not in target:
                ret.append('Push')
                ret.append('Pop')
            if ans == target:
                break
        return ret