class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        y,m,d = int(date1[:4]),int(date1[5:7]),int(date1[8:10])
        d1 = datetime.datetime(y,m,d)
        y,m,d = int(date2[:4]),int(date2[5:7]),int(date2[8:10])
        d2 = datetime.datetime(y,m,d)
        return abs(((d2-d1).days))