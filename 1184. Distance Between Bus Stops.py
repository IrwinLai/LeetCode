class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = 0
        for i in range(min(start,destination),max(start,destination)):
            s += distance[i]
        return min(s,sum(distance)-s)