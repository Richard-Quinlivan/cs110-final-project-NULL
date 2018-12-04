# Galaxy Shooter
## CS 110 Final Project, Semester 1
### Fall 2018

https://github.com/binghamtonuniversity-cs110/final-project-fall18-null

[link to demo presentation slides](#)

### Team: NULL
#### Cindy Guo, Clare Iriarte, Richard Quinlivan

***

## Project Description
Our project is a galaxy shooter type of game. One player is controlling a ship that will shoot a bullet each time they press the spacebar while enemies fire back. The player must avoid the enemy shots. In total there will be three thirty second waves of enemy fighters, and each wave increase in difficultly; for example the final enemy wave will be able to shoot three bullets going in different directions at once. The goal of the game is to defeat all the enemies, and at the end the player will be presented with their “high score” or the amount of enemies they defeated. The player has three lives and if they collide with the enemy’s bullet collides, the player will lose one life. The game is over when the player loses all three lives. 

***    

## User Interface Design 
1. Main Menu Screen

The start screen is the first thing the user sees. There will be two options that will allow the user to either start playing the game (“Play”) or exit the game (“Quit”). 

(Add GUI concept)


2. Gameplay Screen

This screen is where the game takes place. The enemy ships will immediately begin generating once the user presses “Start” on the Main Menu screen. The first wave of enemy ships will shoot bullets that shoot straight ahead. After thirty seconds the second wave of enemy ships will generate, shooting bullets that move up and down. After another thirty seconds, the final wave of enemy ships will generate and shoot three bullets at once, one moving up, one moving down and one moving straight ahead. If the hero ship hits the enemy with a bullet the enemy will disappear. The hero ship loses a life if it is hit by a bullet, collides with an enemy ship, or if an enemy ship reaches the opposite end of the screen without being defeated by the hero ship. If the hero ship loses three lives, the game is over; the amount of remaining lives the hero has will be displayed on the gameplay screen. If the hero ship defeats all the enemies, they have won the game. 

(Add GUI concept)

3. Successful Game Completion Menu

This screen will appear when the hero ship successfully defeats all the enemies. The words “You Win!” will be presented on the screen as well as two buttons:  “Play Again” (which will relaunch the game) and “Quit” (which will quit the game). 

(Add GUI concept) 

4. Game Over Menu

This screen will appear when the hero ship is hit by an enemy bullet three times. The user be presented with the number of enemies they defeated, as well as the option to start the game over by clicking “Play Again” or exit the game by pressing “Quit”.  

(Add GUI concept)

## Program Design
Pygame (https://www.pygame.org/) - A module set incorporating many common game development functions into python, developed by Pete Shinners and Pygame Community. Includes crucial graphical elements as well as a musical playback functionality.	
Addition Libraries/Modules Used:
-

   
* Decide upon a class interface for the classes in your project.
    * A simple drawing that shows the class relationships in your code (see the sample Proposal document for an example).
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* You should have a list of each of your classes with a description.

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.
    * Example:
### Software Lead - [Clare Iriarte]

Worked as integration specialist by helping organize the code for the main game into the proper MVC format, which allowed all portions of the code to be run from a single file. He worked very closely with the back end to develop the high-score database functionality, as well as establish the win- and fail-states for the main game. He also lead the implementation of the ‘sprite’ and ‘group’ classes of pygame into the back end code.

### Front End Specialist - [Cindy Guo]

Front-end lead conducted significant research on using pygame to create visual aspects such as buttons and on-screen text. She used this information to design and program a consistent UI to help the player navigate the title screen, the instructions page, and the “GAME OVER” screen. In addition to implementing the wide majority of the visual element for the UI, she also collaborated with the Software Lead to create a jukebox function that played music and to add sound effects to the menu navigation buttons.

### Back End Specialist - [Richard Quinlivan]

The back end specialist helped with the “Model” portion of BLOCKBUSTERS by writing the major classes that would be used in the main game, as well as implementing major pygame functionality into each of them. He also made headway in major game mechanics such as the basic paddle movement and advanced functionality such as the screen-wrap function for the paddle as it approached the ends of the screen. He collaborated with the Front End Specialist in the implementation of the classes into our Controller file, as well as develop our high-score database.

## Testing
### Menu Testing

First we run Controller() and ensure that the Main Menu opens normally and is functional; the background music should immediately begin playing  We will click the “Start” button to make sure the actual gameplay screen opens and begins immediately generating enemies that shoot bullets. Then we will toggle sound effect by using the “x” and “s” keys. Clicking “x” should turn off sound and “s” should turn sound back on.  Next we will press and hold the right arrow to make sure hero ship moves in the right direction. We will repeat this process using the left arrow, the up arrow and the down arrow to make sure the hero ship moves left, up and down respectfully. Then we will press the spacebar to test to see if the hero ship expels a bullet that move straight and forward; a shooting sound effect should also play normally. 

### Game Testing

When testing gameplay, we have to make sure that enemies “die” or disappear when the colliding with the hero ship’s bullet. The hero ship must also lose a life each time it is shot at, when it collides with the enemy, or when the enemy exits off the opposite end of the screen. The amount of lives the hero ship has left will be indicated with a “live left” countdown visible constantly on the gameplay screen. After 30 seconds a different wave of enemies must also appear on the screen, with three waves total.  The first wave of enemies should shoot bullets that move straight, the second wave should shoot bullets that move up and down, and the third wave should shoot three bullets at once. Background music should remain constant during gameplay, and whenever the hero ship defeats an enemy, collides with an enemy or collides with an enemy bullet an explosion sound effect sound begin playing. 

If the hero ship defeats all the enemies, the Successful Game Completion menu should open normally and display the words “You Win!”. A victory sound effect should also begin playing normally. Each button on the Successful Game Completion Menu should be functional, including “Play Again”, which relaunches the game, and “Quit”, which quits the game with no problems. 

If the hero ship loses all three lives, the Game Over Menu should open normally and display the words “Game Over”, as well as the player’s “high score”, or the amount of enemies they defeated during gameplay. Each button on the Game Over Menu should be functional, including “Play Again”, which relaunches the game, and “Quit”, which quits the game with no problems. A game over sound effect should begin playing immediately once the menu opens. 

We will reopen the game to make sure the “Quit” button on the Main Menu page quits the game successfully. Finally we will click the “X”  button in the top right corner of the window to make sure the game quits properly. This concludes the testing protocol.

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Controller()  | 1) Main Menu opens normally and is functional 2) Background music begins playing |          |
|  2  | Click “Start” button  | When “Start” is pressed the game screen opens and enemies begin generating/shooting at hero |          |
|  3  | Click “x” button | Background music stops playing |          | 
|  4  | Click “s” button | Background music begins playing |          | 
|  5  | Press RIGHT ARROW, hold RIGHT ARROW | The hero ship moves in the right direction without exiting the screen |         | 
|  6  | Press LEFT ARROW, hold LEFT ARROW | The hero ship moves in the left direction without exiting the screen |          |
|  7  | Press UP ARROW, hold UP ARROW | The hero ship moves in the up direction without exiting the screen |          |
|  8  | Press DOWN ARROW, hold DOWN | The hero ship moves in the down direction without exiting the screen |          |
|  9  | Press SPACE BAR | 1) The hero ship shoots out a bullet that shoots straight and forward 2) Shooting sound effect begins playing |          |
|  10  | General playtesting | 1) Enemies “die” or disappear when the hero shoots at them 2) The hero ship loses a life each time it is shot at, as indicated by the “lives left” countdown on the gameplay screen 3) If the enemy collides with the hero ship, the hero ship loses a life 4) If the enemy exits to the opposite end of the screen, the hero loses a life 5) After 30 seconds a different wave of enemies begins generating 6) The first wave of enemies should shoot bullets that move straight, the second wave should shoot bullets that move up and down, and the third wave should shoot three bullets at once 7) Explosion sound effect begins playing whenever the hero ship bullet collides with an enemy ship, when the hero ship and an enemy ship collides, or when a hero ship and an enemy bullet collide |          |
|  11  | Successful Game Completion Menu | 1) If the hero ship defeats all the enemies, the successful game completion menu opens normally and is functional 2) Victory music effect begins playing |          |
|  12  | Test each button on the Successful Game Completion Menu | 1) Menu displays the words “You win!” as well as a “Play Again” button and a “Quit” button 2) “Play Again”relaunches the game with no problems 3) “Quit” quits the game with no problems |          |
|  13  | Game Over Menu | 1) If the hero ship loses all three lives the game over menu opens normally and is functional 2) A game over sound effect should begin playing normally |          |
|  14  | Test each button on the Game Over Menu | 1) Menu displays the words “Game Over” as well as a “Play Again” button and a “Quit” button 2) Menu also displays the number of enemies the hero ship successfully defeated during gameplay 3) “Play Again”relaunches the game with no problems 4) “Quit” quits the game with no problems |          |
|  15  | Re-open game to test QUIT buttons on MAIN MENU pages | When “Quit” is pressed the game quits successfully |          |
|  16  | Click red “X” button in top right corner of window | Game closes out properly |          |
