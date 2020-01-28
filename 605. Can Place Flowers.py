class Solution:
    def canPlaceFlowers(self, A: List[int], n: int) -> bool:
        k = len(A)
        if k == 1:
            return n == 0 if A[0] == 1 else n <= 1
        
        A.append(0)
        A.insert(0,0)
        count = 0
        for i in range(2, k+2):
            if A[i] == 0 and A[i-1] == 0 and A[i-2] == 0:
                count += 1
                A[i-1] = 1
        return count >= n