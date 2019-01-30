#line.py
#1/18/19
#by Josh Pedro
import math
from math import *
from graphics import *
def main():
    win = GraphWin('line',400,400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    l = Line(Point(x1,y1), Point(x2,y2))
    dx = x2-x1
    dy = y2-y1
    slope = dy/dx
    length = sqrt(dx**2 + dy**2)
    m = Point((x1+x2)/2, (y1+y2)/2)
    print("the slope of the line is ",slope)    
    print("the length of the line is ",length)
    print("the midpoint of the line is ",m)
    print(p1)
    print(p2)
    l.draw(win)
    m.setOutline('Cyan')
    m.draw(win)
main()
    
