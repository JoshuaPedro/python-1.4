#square.py 
#by Josh Pedro
#January 4th, 2019
import graphics
from graphics import *
def main():
    win = GraphWin()
    r = Rectangle(Point(80,80), Point(40,40))
    r.setOutline("red")
    r.setFill("red")
    r.draw(win)
#Creates a red filled in square at point (80,80)
    for i in range(1000000000000000000000000000000000000000000000000):
        p = win.getMouse()
        c = r.getCenter()
        win.close()
#Creates a Square that moves when you click it
main()
