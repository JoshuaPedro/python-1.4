#rectangle2.py
#1/18/19
#by Josh Pedro
import math
from math import *
from graphics import *
def main():
    win = GraphWin('rectangle',400,400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    x3 = p3.getX()
    r = Rectangle(Point(x1,y1), Point(x2,y2))
    dx = x2-x1
    dy = y2-y1
    perimeter = 2*(dx + dy)
    area = (dx)*(dy)
    m = Point((x1+x2)/2, (y1+y2)/2)
    print("the area of the rectangle is",area)
    print("the perimeter of the rectangle is ",perimeter)
    print(dx)
    print(dy)
    print(p1)
    print(p2)
    r.draw(win)
    m.setOutline('Cyan')
    m.draw(win)
main()
    
