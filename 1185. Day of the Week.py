from datetime import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        time = datetime(year = year, month = month, day = day)
        weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        return weekday[time.weekday()]