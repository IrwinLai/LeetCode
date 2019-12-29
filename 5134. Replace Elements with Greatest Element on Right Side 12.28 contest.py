class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ret = []
        arr.append(-1)
        tem = -1
        arr = arr[::-1]
        for i in arr[:-1]:
            tem = max(i,tem)
            ret.append(tem)
        return ret[::-1]