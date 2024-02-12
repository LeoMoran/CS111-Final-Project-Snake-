# sprites.py
# This file will hold the designs of each element of 
# the game, in the form of 'sprites'
from graphics import *


class Sprite:
    def __init__(self, win):
        self.win = win
        

    def snekHead(self):
        '''This will show the sprite of the character'''


        # This is the entire Head ---------
        head = Rectangle(Point(35, 20), Point(65, 50))
        head.setFill("green")

        leftEye = Rectangle(Point(40, 25), Point(45, 30))
        leftEye.setFill("Red")

        rightEye = leftEye.clone()
        rightEye.move(15, 0)

        # This draws the Snake
        head.draw(self.win)
        leftEye.draw(self.win)
        rightEye.draw(self.win)

    def snekBody(self):
        # This is the body format
        body = Rectangle(Point(35, 20), Point(65, 50))
        body.setFill("green")
        body.move(0, 30)
        body.draw(self.win)


    def snek(self):
        self.snekHead()
        self.snekBody()

        
    def bug(self):
        '''This will show the sprite of bugs for prey'''

        body = Rectangle(Point(5, 5), Point(20, 20))
        body.setFill("red")
        body.draw(self.win)

    def eyes(self):
        
        head = Rectangle(Point(120, 30), Point(150, 60))
        head.setFill("green")
        head.draw(self.win)

        # Up eyes
        eyes = Polygon(Point(35, 35), Point(35, 45), Point(45, 45), Point(55, 45), Point(55, 35), Point(45, 45))
        eyes.setFill("purple")
        eyes.draw(self.win)

        # Down eyes
        eyes = Polygon(Point(35, 55), Point(35, 45), Point(45, 45), Point(55, 45), Point(55, 55), Point(45, 45))
        eyes.setFill("purple")
        eyes.draw(self.win)

        # Right eyes
        eyes = Polygon(Point(55, 35), Point(45, 35), Point(45, 45), Point(55, 55), Point(45, 55), Point(45, 45))
        eyes.setFill("purple")
        eyes.draw(self.win)

        # Left eyes
        eyes = Polygon(Point(35, 35), Point(45, 35), Point(45, 45), Point(35, 55), Point(45, 55), Point(45, 45))
        eyes.setFill("purple")
        eyes.draw(self.win)

        

        

    def arena1(self):
        '''This will show the platform that the game will be played on'''

        # Rows go from left to right, Colums go from up to down
        row1 = Rectangle(Point(0, 0), Point(600, 30)) 
        row1.draw(self.win)
        rows = [row1]

        for i in range(19):
            newrow = rows[-1].clone()
            rows.append(newrow)
            newrow.move(0, 30)
            newrow.draw(self.win)

        colum1 = Rectangle(Point(0, 0), Point(30, 600)) 
        colum1.draw(self.win)
        colums = [colum1]

        for i in range(19):
            newcolum = colums[-1].clone()
            colums.append(newcolum)
            newcolum.move(30, 0)
            newcolum.draw(self.win)    


    def main(self):
        '''This will showcase the sprites available for the game'''        
        input("Press Enter to end")
win = GraphWin("Game", 601, 601)
Gameplay = Sprite(win)
Gameplay.main()