This project is a fully functional Tic-Tac-Toe game where the computer player plays intelligently. Try It out and see if you can beat the computer.
Python 3.10 is used to built this project. Enjoy


If you want to choose the spot randomly - 

available = game.available_moves()
if len(available) != 0:
	choice = random.choice(available)
      game.board.pop(int(choice))
      game.board.insert(int(choice), self.letter)



Minimax algorythm reference - https://www.youtube.com/watch?v=trKjYdBASyQ&t=107s

Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. It is widely used in two player turn-based games such as Tic-Tac-Toe, Backgammon, Mancala, Chess, etc.
In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible.
Every board state has a value associated with it. In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. The values of the board are calculated by some heuristics which are unique for every type of game.


Improve the efficiency by implementing alpha beta pruning in this algorythm 
