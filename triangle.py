#triangle.py
#1/18/19
#by Josh Pedro
import math
from math import *
from graphics import *
def main():
    win = GraphWin('rectangle',400,400)
    print("click the window three times")
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    x3 = p3.getX()
    y3 = p3.getY()
    l1 = Line(Point(x1,y1), Point(x2,y2))
    l2 = Line(Point(x2,y2), Point(x3,y3))
    l3 = Line(Point(x3,y3), Point(x1,y1))
    dx1 = x2-x1
    dx2 = x3-x2
    dx3 = x1-x3
    dy1 = y2-y1
    dy2 = y3-y2
    dy3 = y1-y3
    a = sqrt(dx1**2 + dy1**2)
    b = sqrt(dx2**2 + dy2**2)
    c = sqrt(dx3**2 + dy3**2)
    s = (a + b + c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print("the area of the Trihangle is",area)
    print(p1)
    print(p2)
    print(p3)
    print(s)
    l1.draw(win)
    l2.draw(win)
    l3.draw(win)
main()
