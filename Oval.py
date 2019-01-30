#rectangle.py
#by Josh Pedro
#January 3rd, 2019
import graphics
from graphics import *
def main():
    win = GraphWin('line')
    o = Oval(Point(50,50), Point(60,100))
    o.setOutline("red4")
    o.draw(win) 
main()
