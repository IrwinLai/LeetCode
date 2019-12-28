class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = 0
        ret = [0 for i in range(num_people)]
        i = 0
        while(candies > 0):
            i += 1
            if i > candies:
                ret[n] += candies
            else:
                ret[n] += i
            candies -= i
            n = (n+1)%num_people
        return ret