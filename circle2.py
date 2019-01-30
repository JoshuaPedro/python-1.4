#circle.py
#by Josh Pedro
#January 4th, 2019
import graphics
from graphics import *
def main():
    win = GraphWin()
    shape = Circle(Point(50,50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
#Creates a red filled in circle at point 50,50
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)
    win.close()
#Creates a circle that moves when you click it
main()
