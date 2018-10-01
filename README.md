# Hacking_Game
This is going to be a game based on the classic Mastermind game and the hacking game from the Fallout games. The point is to have a hacking mini-game for players to use in a TTRPG rather than rolling dice to determine "Did I hack it?"

Design:
This game should randomly generate 5 - 7 random strings depending on difficulty. These strings should have a length of 3 and be using digits 1-3. One of the strings generated will be randomly selected to be considered the "Password". The strings will be put up in the console. Then the person running the program, called the "Player", will be prompted for an input which should be one of the generated strings. If it is the Password then the message "ACCESS GRANTED" and the program exits, otherwise the out put "Correct:2 Wrong Position:0 Incorrect:1" and on a new line "Try Again" then another opportunity will be offered on a new line.

Example:
"221" is the correct string
Below is an example of what a basic input should look like.
113
123
321
221
312
Enter one of the possible passwords:
321
Correct:2 Wrong Position:0 Incorrect:1
Try Again
221
ACCESS GRANTED