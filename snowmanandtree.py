#snowmanandtree.py
#by Josh Pedro
#January 16th, 2019
import graphics
from graphics import *
def main():
    win = GraphWin("snowman and Christmas tree", 900,900)
    torso = Circle(Point(200,550), 160 )
    torso.setFill("White")
    torso.setOutline("black")
    torso.draw(win)
    body = Circle(Point(200, 350), 110)
    body.setFill("White")
    body.setOutline("black")
    body.draw(win)
    arm1 = Line(Point(100,100), Point(199,199))
    arm1.setOutline
    head = Circle(Point(200,200), 90)
    head.setFill("White")
    head.setOutline("black")
    head.draw(win)
    lefteye = Oval(Point(150, 150), Point(177, 177))
    lefteye.setFill("black")
    lefteye.setOutline("brown")
    lefteye.draw(win)
    righteye = Oval(Point(220, 150), Point(247, 177))
    righteye.setFill("black")
    righteye.setOutline("brown")
    righteye.draw(win)
    mouth = Oval(Point(150, 250), Point(247, 277))
    mouth.setFill("black")
    mouth.setOutline("brown")
    mouth.draw(win)
    treetop = Polygon(Point(600, 110), Point(560, 210), Point(570, 210), Point(550, 310), Point(560, 310), Point(540, 410), Point(550, 410), Point(530, 590), Point(670, 590), Point(650, 410), Point(660, 410), Point(640, 310), Point(650,310), Point(630,210), Point(640, 210), Point(600, 110))
    treetop.setFill("green")
    treetop.draw(win)
    treetrunk = Rectangle(Point(590, 590), Point(610, 650))
    treetrunk.setFill("brown")
    treetrunk.draw(win)
main()