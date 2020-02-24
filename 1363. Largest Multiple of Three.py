class Solution:
    def largestMultipleOfThree(self, d: List[int]) -> str:
        def helper(arr,k):
            # could delete one
            if dic[arr[0]] >= k:
                dic[arr[0]] -= k
            elif dic[arr[0]] == 0:
                helper(arr[1:],k)
            # need to delete two, but could only delete one
            elif dic[arr[0]] == 1:
                dic[arr[0]] -= 1
                helper(arr[1:],1)
        
        dic = collections.Counter(d)
        s = 0
        for k in dic:
            s += dic[k]*k
        if s%3 == 1:
            if dic[1] + dic[4] + dic[7] >= 1:
                helper([1,4,7],1)
            else:
                helper([2,5,8],2)
                
        elif s%3 == 2:
            if dic[2] + dic[5] + dic[8] >= 1:
                helper([2,5,8],1)
            else:
                helper([1,4,7],2)
        
        l = sorted(list(dic.keys()),reverse = True)
        res = ""
        for i in l:
            res += str(i)*dic[i]
        if set(l) == {0}:
            return '0'
        return res