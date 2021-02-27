class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(boxes)
        if set(boxes) == {'0'}:
            return [0]*len(boxes)
        
        pos,ans = [],[]
        for i in range(len(boxes)):
            if boxes[i] == '1':
                pos.append(i)
        
        for i in range(len(boxes)):
            tem = 0
            for j in range(len(pos)):
                tem += abs(pos[j] - i)
            ans.append(tem)
    
        return ans
            