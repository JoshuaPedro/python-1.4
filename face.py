#target.py
#by Josh Pedro
#January 4th, 2019
import graphics
from graphics import *
def main():
    win = GraphWin("face", 600,600)
    head = Circle(Point(300,300), 90)
    head.setFill("White")
    head.setOutline("brown")
    head.draw(win)
    lefteye = Oval(Point(250, 250), Point(277, 277))
    lefteye.setFill("black")
    lefteye.setOutline("brown")
    lefteye.draw(win)
    righteye = Oval(Point(320, 250), Point(347, 277))
    righteye.setFill("black")
    righteye.setOutline("brown")
    righteye.draw(win)
    mouth = Oval(Point(250, 350), Point(347, 377))
    mouth.setFill("black")
    mouth.setOutline("brown")
    mouth.draw(win)
main()
