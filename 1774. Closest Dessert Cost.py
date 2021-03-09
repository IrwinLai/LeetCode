class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        temcost = [0]
        for cost in toppingCosts:
            tem = []
            for i in temcost:
                tem.append(i + cost)
                tem.append(i + cost * 2)
            temcost.extend(tem)
        print(temcost)
        ans = 0
        temmin = 10000
        for base in baseCosts:
            for cost in temcost:
                if temmin == abs(base+cost-target) and base+cost < target:
                    ans = base+cost
                if temmin > abs(base+cost-target):
                    temmin = abs(base+cost-target)
                    ans = base+cost
        return ans
            