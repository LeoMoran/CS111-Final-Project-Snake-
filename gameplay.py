# gameplay.py
# This will hold the "rules" of the game for when the snake 
# extends or dies, it will also be in control of when the game 
# is over and end screen is displayed.
from matplotlib.colors import rgb2hex
from graphics import *
from food import Food
from snake import Snake  
class game:
    def __init__(self, win):
        '''This sets all of the variables needed for the functions to work'''
        self.win = win # Acts as the main window for where the game is played on
        self.player = Snake(self.win) # Creates the snake and allows us to use the functions for it's class
        self.bug = Food(self.win) # Creates the food and allows us to use the functions for it's class
        self.arena1() # This builds the arena for the game
        self.gameOver = False # Act's as a value to see if the game should continue or end
        self.speed = 1


    def playGame(self):
        '''This will actualy "play" the game in the order of most importance, taking 
        functions from the diffrent classes from their respective files.'''
        while not self.gameOver:
            time.sleep(0.3 / self.speed) # This prevents the game from going through in an instant

            self.player.movement() # This sets up the movement for the player

            headx1 = self.player.getHeadx1() # gets the x value of the first point of the head of the snake
            heady1 = self.player.getHeady1() # gets the y value of the first point of the head of the snake
            headx2 = self.player.getHeadx2() # gets the x value of the secound point of the head of the snake
            heady2 = self.player.getHeady2() # gets the y value of the secound point of the head of the snake

            if self.player.getGameStatus() == True: # Checks to see if the game has ended for the snake before ending it on gameplay
                self.overScreen()
                self.gameOver = True # sets the value true so that the while loop for the playGame function ends

            if self.bug.eaten(headx1, heady1, headx2, heady2) == True: # Checks with the food if it has been eaten
                self.player.eat() # notifies the snake class to extend by one
                self.speed = self.speed + 0.3


    def overScreen(self):
        '''This will display text stating the the game is over'''
        tex = Text(Point(300, 300), "GAME OVER")
        tex.setTextColor("white")
        tex.setSize(30)
        tex.draw(self.win)
        time.sleep(3)


    def arena1(self):
        '''This will show the platform that the game will be played on'''

        self.win.setBackground("grey")
        # Rows go from left to right, Colums go from up to down
        row1 = Rectangle(Point(0, 0), Point(600, 30))
        row1.draw(self.win)
        rows = [row1]

        for i in range(19): # This for loop creates every row on the arena and draws each one before adding them to a list
            newrow = rows[-1].clone()
            rows.append(newrow)
            newrow.move(0, 30)
            newrow.draw(self.win)

        colum1 = Rectangle(Point(0, 0), Point(30, 600)) 
        colum1.draw(self.win)
        colums = [colum1]

        for i in range(19): # This for loop creates every colum on the arena and draws each one before adding them to a list
            newcolum = colums[-1].clone()
            colums.append(newcolum)
            newcolum.move(30, 0)
            newcolum.draw(self.win)


win = GraphWin("Snake.py", 601, 601) # Creates the window for the game, must be 601, 601 for the game to work, can use vaiables to make this bigger/smaller
mainGame = game(win)
mainGame.playGame() # This plays the game