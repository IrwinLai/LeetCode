class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for i in strs:
            d["".join(sorted(list(i)))].append(i)
        return list(d.values())