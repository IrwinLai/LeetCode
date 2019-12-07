class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for item in cpdomains:
            item = item.split(" ")
            num = int(item[0])
            sub = item[1].split(".")
            for i in range(len(sub)):
                d[".".join(sub[i:])] = d.get(".".join(sub[i:]),0) + num
                
        return (list(map(lambda x:str(d.get(x)) + " " + x, list(d.keys()))))
                
                