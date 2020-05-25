class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'
        num = list(num)
        stack = []
        for i in range(len(num)):
            while True:
                if not stack or k == 0:
                    break
                if stack[-1] > num[i]:
                    stack.pop()
                    k -= 1
                else:
                    break
            stack.append(num[i])
            
        if k > 0:
            for i in range(k):
                stack.pop()
                
        return str(int("".join(stack)))         