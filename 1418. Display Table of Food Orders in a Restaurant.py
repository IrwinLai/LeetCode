class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food = set()
        d = {}
        title = ['Table']
        for order in orders:
            if order[2] not in food:
                food.add(order[2])
            if order[1] not in d:
                d[order[1]] = {}
            d[order[1]][order[2]] = d[order[1]].get(order[2],0) +1

        food = sorted(list(food))
        title.extend(food)
        ans = [title]
        for i in sorted(list(d.keys()),key = lambda x:int(x)):
            tem = [i]
            for j in food:
                tem.append(str(d[i].get(j,0)))
            ans.append(tem)
        return ans