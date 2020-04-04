class Solution:
    def checkOverlap(self, r: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def d(xa,ya,xb,yb):
            return ((xa-xb)**2+(ya-yb)**2)**0.5
        if (x1 <= xc <= x2 and y1-r <= yc <= y2+r) or (x1-r <= xc <= x2+r and y1 <= yc <= y2):
            return True
        if d(xc,yc,x1,y1) <= r or d(xc,yc,x2,y2) <= r or d(xc,yc,x1,y2) <= r or d(xc,yc,x2,y1) <= r:
            return True
        return False