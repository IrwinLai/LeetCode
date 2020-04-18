class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def bfs(check, times):
            time = 1
            tem = check
            while time < times:
                tem = []
                for i in check:
                    if i[-1] == "a":
                        tem.append(i+"b")
                        tem.append(i+"c")
                    if i[-1] == "b":
                        tem.append(i+"a")
                        tem.append(i+"c")
                    if i[-1] == "c":
                        tem.append(i+"a")
                        tem.append(i+"b")
                check = tem
                time += 1
            if time == times:
                return tem
            
        l = sorted(bfs(['a','b','c'],n))
        if k > len(l):
            return ""
        else:
            return l[k-1]