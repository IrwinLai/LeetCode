class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        tem = [i for i in range(len(mat))]
        tem.sort(key = lambda x:mat[x])
        return tem[:k]