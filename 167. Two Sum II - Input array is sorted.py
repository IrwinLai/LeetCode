class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while True:
            tem = numbers[i] + numbers[j]
            if tem == target:
                return [i+1,j+1]
            elif tem < target:
                i += 1
            else:
                j -= 1
        