#dice.py
#by Josh Pedro
#January 16th 2019
import graphics
from graphics import *
def main():
    win = GraphWin("dice roller", 500,500)
    d1 = Rectangle(Point(40, 80), Point(80, 40))
    d1.setFill('gold')
    c1 = Circle(Point(60, 60),5)
    c1.setFill('orange')
    d1.draw(win)
    c1.draw(win)
    d2 = d1.clone()
    d2.move(160, 0)
    d2.draw(win)
    c2 = c1.clone()
    c2.move(169, 11)
    c2.draw(win)
    c3 = c2.clone()
    c3.move(-18,-21)
    c3.draw(win)
    d3 = d2.clone()
    d3.move(180, 0)
    d3.draw(win)
    c4 = c1.clone()
    c4.move(340,0)
    c4.draw(win)
    c5 = c2.clone()
    c5.move(184,-1)
    c5.draw(win)
    c6 = c3.clone()
    c6.move(177, -1)
    c6.draw(win)
    d4 = d1.clone()
    d4.move(0, 100)
    d4.draw(win)
    c7 = c2.clone()
    c7.move(-180,100)
    c7.draw(win)
    c8 = c7.clone()
    c8.move(22, 0)
    c8.draw(win)
    c9 = c8.clone()
    c9.move(0,-22)
    c9.draw(win)
    c10 = c9.clone()
    c10.move(-22,0)
    c10.draw(win)
    d5 = d2.clone()
    d5.move(0, 100)
    d5.draw(win)
    c11,c12,c13,c14 = c7.clone(), c8.clone(), c9.clone(),c10.clone()
    c11.move(160, 0)
    c12.move(160, 0)
    c13.move(160, 0)
    c14.move(160, 0)
    c15 = c1.clone()
    c15.move(-180,100)
    c16 = c14.clone()
    c16.move(11,11)
    c14.draw(win)
    c11.draw(win)
    c12.draw(win)
    c13.draw(win)
    c16.draw(win)
main()
    
