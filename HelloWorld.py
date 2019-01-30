#HelloWorld.py
#by Josh Pedro
#January 4th, 2019
import graphics
from graphics import *
def main():
    win = GraphWin('text')
    t = Text(Point(100,100), "Hello World!")
    t.setFace("courier")
    t.setSize(16)
    t.setStyle("italic")
    t.draw(win)
main()
