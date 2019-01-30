#CircIntersection.py
#by Joshua Pedro
#January 17th, 2019
#calculates the  intersection of a circle with a horizontal line
import math
import graphics
from graphics import *
def main():
    win = GraphWin('Shapes')
    win.setCoords(-10, -10, 10, 1 0)
    y = eval(input("input the y value. "))
    r = eval(input("enter the radius. "))
    circ = Circle(Point(0, 0), r)
    x = math.sqrt((r**2)-(y**2))
    x1 = (math.sqrt((r**2)-(y**2)))*-1
    line = Line(Point(10, y), Point(-10,y))
    circ.setOutline("green")
    circ.setFill('blue')
    circ.draw(win)
    line.draw(win)
    print("the x intersection is ",x)
    print("the x1 intersection is",x1)
    P1 = Point(x,y)
    P2 = Point(x1,y)
    P1.setOutline("red")
    P2.setOutline("red")
    P1.draw(win)
    P2.draw(win)
main()

