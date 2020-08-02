class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        ma = max(arr)
        n = len(arr)
        
        if k >= n:
            return ma
        
        arr = deque(arr)
        count = 0
        while count < k:
            a = arr[0]
            b = arr[1]
            arr.popleft()
            arr.popleft()
            
            if a <= b:
                count = 1
                arr.appendleft(b)
                arr.append(a)
            else:
                count += 1
                arr.appendleft(a)
                arr.append(b)
            
            if count == k or arr[0] == ma:
                return arr[0]
            
        return arr[0]
            