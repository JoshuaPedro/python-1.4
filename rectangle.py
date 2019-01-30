#rectangle.py
#by Josh Pedro
#January 3rd, 2019
import graphics
from graphics import *
def main():
    win = GraphWin('rectangle')
    r = Rectangle(Point(20,20), Point(40,40))
    r.setFill(color_rgb(0,255,150))
    r.setWidth(3)
    r.draw(win)
main()
