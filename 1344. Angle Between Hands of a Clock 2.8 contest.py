class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ang = abs(((hour+minutes/60)%12)*30 - minutes*6)
        return (min(ang,360-ang))