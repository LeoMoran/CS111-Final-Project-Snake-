# snake.py
# This will hold the controls that the player will have over the snake, 
# as well as how the snake moves
from graphics import * 
class Snake:
    def __init__(self, win): 
        '''This sets all of the variables that will be needed between the diffrent functions'''
        self.win = win # Acts as the main window for where the snake is drawn on

        self.gameOver = False

        # The starting position of snake
        # Head
        self.headx1 = 120 
        self.heady1 = 30

        self.headx2 = 150
        self.heady2 = 60

        # Creates the shape of the snake's head, eyes, and body
        self.head = Rectangle(Point(self.headx1, self.heady1), Point(self.headx2, self.heady2))
        self.head.setFill("yellow")

        self.snekList = [self.head]

        self.moveList = ['d', 'd', 'd', 'd', "d"]

        self.newDirection = 'd'

        # Draws the initial snake
        self.head.draw(self.win)

        # This draws the eyes of the snake
        self.eyes = Polygon(Point(self.headx1 + 25, self.heady1 + 5), Point(self.headx1 + 15, self.heady1 + 5), Point(self.headx1 + 15, self.heady1 + 15), Point(self.headx1 + 25, self.heady1 + 25), Point(self.headx1 + 15, self.heady1 + 25), Point(self.headx1 + 15, self.heady1 + 15))
        self.eyes.setFill("purple")
        self.eyes.draw(self.win)

        for segment in range(2): # This creates a new segment of the snake when it's first being created
            body = self.snekList[-1].clone()
            body.move(-30, 0)
            body.setFill("green")
            self.snekList.append(body)
            body.draw(self.win)


    def movement(self):
        '''This will dictate the movement that the snake will take'''

        temp = self.win.checkKey()
        # This should make any other key inpust that are not wasd into '', so that 
        # the game does not break if the player enter the wrong key
        if temp != 'w' and temp != 'a' and temp != 's' and temp != 'd': 
            temp = ''


        if self.gameOver != True: # Checks if the game has ended before running the loop
            if not temp == '': # Checks if any key has been inputted before running it, ignoring any empty key presses
                self.newDirection = temp

                # a is left | d is right | w is up | s is down
            if self.newDirection == 'a' and self.moveList[-1] == 'd': # If snake is moving to the left/right, it cannot double back on itself
                self.moveList.append(self.moveList[-1]) # Uses the last key as the new direction
                self.snek()

            elif self.newDirection == 'd' and self.moveList[-1] == 'a': # If snake is moving to the left/right, it cannot double back on itself
                self.moveList.append(self.moveList[-1]) # Uses the last key as the new direction
                self.snek()

            elif self.newDirection == 's' and self.moveList[-1] == 'w' or self.newDirection == 's' and self.moveList[0] == '': # If snake is moving up/down, it cannot double back on itself
                self.moveList.append(self.moveList[-1]) # Uses the last key as the new direction
                self.snek() 

            elif self.newDirection == 'w' and self.moveList[-1] == 's': # If snake is moving up/down, it cannot double back on itself
                self.moveList.append(self.moveList[-1]) # Uses the last key as the new direction
                self.snek()

            else:
                if self.newDirection == 'w':
                    self.moveList.append(self.newDirection)
                    self.snek()

                elif self.newDirection == 's':
                    self.moveList.append(self.newDirection)
                    self.snek()
                    
                elif self.newDirection == 'a':
                    self.moveList.append(self.newDirection)
                    self.snek()

                elif self.newDirection == 'd':
                    self.moveList.append(self.newDirection)
                    self.snek()
        return self.gameOver


    def gameCheck(self): # The game does not end if the head overlaps the body
        '''This checks to make sure that the next move is valid, if it's not then it sets 
        the variable self.gameOver to True in order to end the movement function'''
        direction = self.moveList[-1] # Takes the newest move before it has been used
        
        # creates copies of the current position of the head
        headx1 = self.headx1 
        heady1 = self.heady1
        headx2 = self.headx2
        heady2 = self.heady2
        
        # These if and elif statements move the copies of the heads original position in order to know where
        # it will be oing next
        if direction == 'w':
            heady1 += -30
            heady2 += -30

        elif direction == 's':
            heady1 += 30
            heady2 += 30            

        elif direction == 'a':
            headx1 += -30
            headx2 += -30

        elif direction == 'd':
            headx1 += 30
            headx2 += 30
        # These check if any of the cordinates for the head ever goes out of bounds, if it does then it sets
        # self.gameOver = True to end the while loop for the movement of the snake.
        if headx1 < 0: 
            self.gameOver = True
        
        elif heady1 < 0:
            self.gameOver = True
        
        elif heady2 > 600:
            self.gameOver = True

        elif headx2 > 600:
            self.gameOver = True    


        # this for loop checks to see if the center of the segments of the snake ever overlap with the 
        # center of the head, if it does then the game would end.
        for segment in self.snekList: 
            # When checking the center of the body segment, the body only ever moves after 
            # the body extends, meaning that this is only checking the last point only.
            bodyLocation = segment.getCenter()
            bodyLocationx = bodyLocation.getX()
            bodyLocationy = bodyLocation.getY()
            headLocation = self.snekList[0].getCenter()
            headLocationx = headLocation.getX()
            headLocationy = headLocation.getY()

            
            if segment != self.head and bodyLocationx == headLocationx and bodyLocationy == headLocationy:
                self.gameOver = True


    def snek(self):
        '''This takes the new move and shortens the list to it's appropriate size before 
        distributing eave move to it's rightful segment of the snake'''
        self.gameCheck() # First checks if the game will continue or not, to prevent further moves from the movement function
        if len(self.moveList) > len(self.snekList) + 1: # This makes sure that the movelist will always remain the same length as the snake list
            self.moveList.pop(0) # removes the last move in the list, which is actually the first move in the list since I add the new moves to the end of the list with .append()
            
        # this for loop will disperse the moves according to the segment of the snake list, 
        # differing between the head and body since I have to keep track of the head for other functions, it 
        # doesn't matter for the body
        for segment in range(len(self.snekList)): 
            if segment == 0:
                self.snekHead(self.moveList[-1]) # the head recives the newest move, which is at the end of the list

            else:
                # The body segment will recive the move from the moove list in receding order, so the 1st segment 
                # gets the 2nd move, and so on. Then I also add which segment is reciving that move by specifyng 
                # which segment within its parameter
                self.snekBody(self.moveList[len(self.moveList) - segment - 1], segment) 


    def snekHead(self, direction):
        '''This will move the head of the snake according to the given direction'''
        self.head.undraw() # removes the last head to clean up prior to the new head
        self.eyes.undraw()
        # Depending on the direction given, it will move the head accordingly while also updating
        # the head's cordinates since .move() doesn't do that anyways... ugh

        if direction == 'w':
            self.head.move(0, -30)
            self.heady1 += -30
            self.heady2 += -30
            self.eyes = Polygon(Point(self.headx1 + 5, self.heady1 + 5), Point(self.headx1 + 5, self.heady1 + 15), Point(self.headx1 + 15, self.heady1 + 15), Point(self.headx1 + 25, self.heady1 + 15), Point(self.headx1 + 25, self.heady1 + 5), Point(self.headx1 + 15, self.heady1 + 15))
        
        elif direction == 's':
            self.head.move(0, 30)
            self.heady1 += 30
            self.heady2 += 30
            self.eyes = Polygon(Point(self.headx1 + 5, self.heady1 + 25), Point(self.headx1 + 5, self.heady1 + 15), Point(self.headx1 + 15, self.heady1 + 15), Point(self.headx1 + 25, self.heady1 + 15), Point(self.headx1 + 25, self.heady1 + 25), Point(self.headx1 + 15, self.heady1 + 15))

        elif direction == 'a':
            self.head.move(-30, 0)
            self.headx1 += -30
            self.headx2 += -30
            self.eyes = Polygon(Point(self.headx1 + 5, self.heady1 + 5), Point(self.headx1 + 15, self.heady1 + 5), Point(self.headx1 + 15, self.heady1 + 15), Point(self.headx1 + 5, self.heady1 + 25), Point(self.headx1 + 15, self.heady1 + 25), Point(self.headx1 + 15, self.heady1 + 15))

        elif direction == 'd':
            self.head.move(30, 0)  
            self.headx1 += 30
            self.headx2 += 30
            self.eyes = Polygon(Point(self.headx1 + 25, self.heady1 + 5), Point(self.headx1 + 15, self.heady1 + 5), Point(self.headx1 + 15, self.heady1 + 15), Point(self.headx1 + 25, self.heady1 + 25), Point(self.headx1 + 15, self.heady1 + 25), Point(self.headx1 + 15, self.heady1 + 15))
     
        
        self.head.draw(self.win) # Draws new head
        self.eyes.setFill("purple") # Fills in the new polygon
        self.eyes.draw(self.win) # Redraws the eyes as a new shape dependent of the head


    def snekBody(self, direction, segment): 
        '''This moves the body according to what segment it is and what direction that it is given'''
        self.snekList[segment].undraw() # removes old body to clean up for the new body
        
        # Depending on the direction given, it will move the body accordingly
        if direction == 'w':
            self.snekList[segment].move(0, -30)

        elif direction == 's':
            self.snekList[segment].move(0, 30)

        elif direction == 'a':
            self.snekList[segment].move(-30, 0)

        elif direction == 'd':
            self.snekList[segment].move(30, 0)

        self.snekList[segment].draw(self.win) # Draws the new body segment


    def eat(self): 
        '''This will cause the snake to grow by one segment for everytime tht it is called'''
        movey = 0
        movex = 0

        # Checks what was the oldest move was in order to know where to place the new 
        # segment right behind the last body segment
        if self.moveList[1] == 'w':
            movey = 30

        elif self.moveList[1] == 's':
            movey = -30          

        elif self.moveList[1] == 'a':
            movex = 30

        elif self.moveList[1] == 'd':
            movex = -30
        
        body = self.snekList[-1].clone() # Takes a copy of the last body segment
        body.move(movex, movey) # Moves the location of this new body segment in accordance to the last move
        body.setFill("green") # Sets it to green just in case
        body.draw(self.win) # Draws new body segment

        self.snekList.append(body) # adds the newest body segment to the list


# These get functions will be primaryily used in gameplay.py to check the location 
# of the head and the status of the snake
    def getHeadx1(self):
        return self.headx1
    def getHeady1(self):
        return self.heady1

    def getHeadx2(self):
        return self.headx2
    def getHeady2(self):
        return self.heady2
    
    def getGameStatus(self):
        return self.gameOver