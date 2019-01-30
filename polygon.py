#rectangle.py
#by Josh Pedro
#January 3rd, 2019
import graphics
from graphics import *
def main():
    win = GraphWin('polygon',900,900)
    win.setCoords(0,0, 11,11)
    shape = Polygon(Point(5,5), Point(10,10), Point(5,10), Point(10,5)) 
    shape.setFill("orange")
    shape.draw(win)
main()
