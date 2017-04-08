readme.txt

Danielle Eisen, Nov 21 2016

This Backgammon game allows users to play against either another person
(on the same device) or against the computer, by inputting the category
of each player in the terminal window.

Human players click on the piece they wish to move and then the desired
destination to move the piece to. Player 1 plays using the white pieces
in a counterclockwise direction, and player 2 uses the brown pieces and
moves in clockwise direction. Computer players also select pieces which
move, if there are any computer players.

The program is organized into six different classes for different parts
of the game. It is run by the Board class, which imports other classes,
including the Wedge class, the Player class, and the Center class. Each
of those classes imports other classes - the Piece and the Die classes.

Structuring the program with separate classes, each in its own separate
file, allows the different parts of the game to function separately yet
still depend on each other.

At this point, the program works to allow movement and capturing pieces
when both players are human, but runs into some difficulties when there
is a computer player. It glitches when there are no moves that are both
available and allowed for the current player. It also does not have any
mechanism for the end of the game yet, and does not give a player extra
plays when they roll a double.

This program uses the Python graphics module written by John Zelle, and
the random Python library.