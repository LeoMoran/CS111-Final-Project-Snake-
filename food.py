# food.py
# This file will control where the food will spawn within the gameboard, 
# with the food going closer to the player body the longer the snake gets.
# Hopefully, the bug will also be able to move as well.
from graphics import * 
import random 
class Food:
    def __init__(self, win):
        '''This sets all of the variables that will be needed between the diffrent functions'''
        self.win = win # Acts as the main window for where the food is drawn on
        
        self.bugx1 = 300 # x1, y1 are top left
        self.bugy1 = 300

        self.bugx2 = 330 # x2, y2 are bottom right
        self.bugy2 = 330

        self.counter = 0 # This will increase the more times that the food gets eaten, causing 
                         # the game to become more difficult

        self.oldranx = 0 # Remembers what the last value of ranx
        self.oldrany = 0 # Remembers what the last value of rany

        self.body = Rectangle(Point(self.bugx1, self.bugy1), Point(self.bugx2, self.bugy2))
        self.body.setFill("red")
        self.body.draw(self.win)


    def eaten(self, headx1, heady1, headx2, heady2):
        '''This checks to see if the food has been "eaten" by the head of the snake before 
        deciding to start the foodSpawn() function and undraw the food'''
        
        if headx1 == self.bugx1 and heady1 == self.bugy1 and headx2 == self.bugx2 and heady2 == self.bugy2: # Checks to make sure that the head of the snake is completely overlaping the body of the bug/food

            if self.counter / 2 != self.counter // 2: # Checks to see if the counter is odd or even before changing the sign, in order to prevent the game from going only in one side
                counterSign = -1
            else:
                counterSign = 1

                
            self.counter = abs(self.counter) + 1
            self.counter = self.counter * counterSign # This make sure that it doesn't just stick to the right as the game progresses

            if abs(self.counter) > 10:
                self.counter = (self.counter / self.counter) * 7

            self.body.undraw()
            self.foodSpawn()           
            return True
        

    def foodSpawn(self):
        '''Once it has been activated, it will take a random intiger that is within the arena 
        and add the counter value to determine the new location of the new food piece'''

        ranx = random.randint(5, 15) + self.counter # This will be used in the left point
        rany = random.randint(5, 15) # This will be used in the top point
        
        while self.oldranx == ranx and self.oldrany == rany: # This prevents the food from spawing in it's exact spot twice
            ranx = random.randint(5, 15) + self.counter
            rany = random.randint(0, 19)

        
        if ranx > 19: # This makes sure that the food never spawns out of bounds
            ranx = 19
        if rany > 19:
            rany = 19
        if ranx < 0:
            ranx = 0
        if rany < 0:
            rany = 0


        self.bugx1 = ranx * 30
        self.bugx2 = self.bugx1 + 30

        self.bugy1 = rany * 30
        self.bugy2 = self.bugy1 + 30

        self.body = Rectangle(Point(self.bugx1, self.bugy1), Point(self.bugx2, self.bugy2))
        self.body.setFill("red")

        self.body.draw(self.win)