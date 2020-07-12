class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        print(date)
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        date[0] = date[0][:-2]
        if int(date[0]) < 10:
            date[0] = '0'+date[0]
            
        date[1] = str(month.index(date[1])+1)
        if int(date[1]) < 10:
            date[1] = '0'+date[1]
            
        ans = date[2]+'-'+date[1]+'-'+date[0]
        
        return ans