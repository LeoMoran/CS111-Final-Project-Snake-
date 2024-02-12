Slippery Little Snake

Made by me! Leo Moran

The functionality of each file
    graphics.py is used for creating the graphics of the object, as well as 
it's cordinates for each object. This file was made by John Zelle, and is an open source 
file that I use within my game.

    sprites.py holds the graphic design codes of each element or 'sprite' for the game 
before implementing it into their respective files such as snake.py, food.py, or gameplay.py.

    food.py not handles the spawn of the food once it has been eaten, as well as it's difficulty 
as it continues to be eaten by the snake, which it learns by comparing the cordinates of the snake 
head with the cordinates of the food. The game becomes more and more diffult by spawning the food 
closer to the edge of the map.

    The food spawn would be where the AI is located since it will spawn further away from the center 
the more it gets eaten, but near the end of the game it does not only spawn near the edge so that it 
doesn't just spawn in the same two positions over and over again.

    snake.py handels the movement of the snake as well as to see if the game will end. It does 
this by comparing the cordinates of the snake with the boundaries of the game, which is set as 
0-600, so that if the snake ever goes ot of bounds, the game would end. Annother way the game 
would end would be by having the center of the head overlap with any of it's body segments. This 
file will also enlongate the snake by being invoked from gameplay.py, and does this by appending 
annother segment to self.snekList.

    gameplay.py is the file that works with both snake.py and food.py in order to get the game 
working. It does this by creating a class where an instance variable would equal to the class 
of Snake and Food, in order to transfer data between the two classes and determine if the 
game will continue or end. The order that the game operates can be seen in the playGame 
function in the game class, where it first moves the snake, then checks if the game ending 
conditions of snake has been met before comparing the snake heads current position with the
position of the food to see if the food has been eaten or not. If it has then food.py  
will invoke the eaten function and snake.py will invoke the eat function. 

Once the game has ended, the overScreen function is used and the game is set to a standstill 
for a short while before closing.


How to play the game. 
This should include information such as what extra files, if any, are needed to run the program:

In order to run the game, enter into the terminal "python3 gameplay.py" then you click on the new 
window and use the keys wasd to control the direction of the snake. If you have issues with 
running it, you may not have matplotlib installed, in which case just type "pip install matplotlib" 
into the same terminal, wait for it to load, then try running the game again.

Rules-
If you go out of the map or have your head overlap with the body, you lose.
Every time that the head overlaps with the red dot (the food/bug), you body will extend 
by one segment and you also become slightly faster.

Once the game ends it will display "Game Over" in blue in the center of the screen before 
closing the window, you then re-enter "python3 gameplay.py" into the terminal and click on 
the window to play again


A brief description of any known bugs or issues with the program:

The body can spawn out of place if you position the 2nd to last 
segment in a diagonal movement.