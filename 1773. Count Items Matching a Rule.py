class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dkey = {'type':0,'color':1,'name':2}
        ans = 0
        for item in items:
            if item[dkey[ruleKey]] == ruleValue:
                ans += 1
        return ans