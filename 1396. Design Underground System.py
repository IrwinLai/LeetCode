class UndergroundSystem:

    def __init__(self):
        self.start = {}
        self.end = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName,t]

    def checkOut(self, id: int, e: str, et: int) -> None:
        s,st = self.start[id]
        if (s,e) in self.end:
            x,y = self.end[(s,e)]
            self.end[(s,e)] = [x+et-st,y+1]
        else:
            self.end[(s,e)] = [et-st,1]

    def getAverageTime(self, s: str, e: str) -> float:
        if (s,e) in self.end:
            x,y = self.end[(s,e)]
            return x/y
        return 0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)