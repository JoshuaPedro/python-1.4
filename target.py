#target.py
#by Josh Pedro
#January 4th, 2019
import graphics
from graphics import *
def main():
    win = GraphWin("target", 600,600)
    win.setBackground("lime green")
    shape5 = Circle(Point(300,300), 100)
    shape5.setOutline("white")
    shape5.setFill("white")
    shape5.draw(win)
    shape4 = Circle(Point(300,300), 80)
    shape4.setOutline("black")
    shape4.setFill("black")
    shape4.draw(win)
    shape3 = Circle(Point(300,300), 60)
    shape3.setOutline("blue")
    shape3.setFill("blue")
    shape3.draw(win)
    shape2 = Circle(Point(300,300), 40)
    shape2.setOutline("red")
    shape2.setFill("red")
    shape2.draw(win)
    shape1 = Circle(Point(300,300), 20)
    shape1.setOutline("gold")
    shape1.setFill("gold")
    shape1.draw(win)
#Creates a gold filled in circle at point 300,300
main()
