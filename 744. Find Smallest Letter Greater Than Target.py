class Solution:
    def nextGreatestLetter(self, L: List[str], t: str) -> str:
        L.append(t)
        L = list(set(L))
        L.sort()
        tem = L.index(t)
        return L[tem+1] if tem < len(L)-1 else L[0]
