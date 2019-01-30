#rectangle.py
#by Josh Pedro
#January 3rd, 2019
import graphics
from graphics import *
def main():
    win = GraphWin('line')
    l = Line(Point(100,100), Point(100,200))
    l.setOutline("red4")
    l.setArrow("first")
    l.draw(win) 
main()
