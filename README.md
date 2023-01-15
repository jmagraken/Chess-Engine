## Chess-Engine

*This project is still in its very early stages. As it stands, this chess engine is about as good as someone who has only played a few games of chess.*

To try the program, run ChessEngine.py with the command line argument "py .\ChessEngine.py [parameter]", replacing "[parameter]" with either "botvbot" for the computer to simulate an entire chess game, or "botvhuman" to play against the bot. 

At this point, the program is unable to recognize checkmate - it will just fail to perform a move if a checkmate occurs.

# botvbot mode

In this mode, the computer will rapidly simulate a chess game between black, which makes random moves, and white, which makes somewhat intelligent moves. Hence, white usually wins, although they may draw.

# botvhuman mode

In this mode, you play as black. To perform a move, you must input the beginning and ending position of the move to the command line. For example, to move from a7 to a6, enter "a7 a6". Note that queen promition is supported, but other special chess moves (castling, en passant) aren't yet. Every time a move is performed, a plain-text representation of the board is printed out (see photo below). All the pieces are abbreviated to two letters, so, for example, 'black queen' becomes 'bq', and an 'x' represents a free space.  







