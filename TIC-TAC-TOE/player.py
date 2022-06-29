import time
from abc import ABC, abstractmethod

from math import inf


class Player(ABC):

    def __init__(self):
        self.letter = ""

    @abstractmethod
    def choose_slot(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        while True:
            letter = input("Enter the letter that you want to play with - (X or O): ")
            if letter.upper() not in ["X", "O"]:
                print("Invalid Letter! Please enter again")
            else:
                break
        self.letter = letter.upper()

    def choose_slot(self, game):
        while True:
            user_choice = input(f"Enter the slot that you want to choose: ")
            if not user_choice.isnumeric():
                print("Invalid Input!")
                time.sleep(3)
            elif user_choice not in game.available_moves():
                print("You do not have that choice available.")
                time.sleep(3)
            else:
                game.board.pop(int(user_choice))
                game.board.insert(int(user_choice), self.letter)
                break


class ComputerPlayer(Player):
    def __init__(self, human_letter):
        super().__init__()
        letters = ["X", "O"]
        letters.remove(human_letter)
        self.letter = letters[0]

    def choose_slot(self, game):
        # make a copy of the current game
        dummy_game = game
        # get the available moves remaining for a player
        available = dummy_game.available_moves()
        # We are considering computer to be a max player, worst score for a max player will be negative infinity
        # Hence our starting point will be negative infinity. We will check which of the available slots is
        # the best possible move for the current scenario by simulating the game until one of the player wins.
        bestScore, bestMove = -inf, 0
        # for each available slot, we make the move, then run the minimax algo to get the score of that slot.
        # if any other slot has a better score, it is stored in the bestScore variable and the corresponding
        # move is stored in bestMove variable. So after the loop we will get the best move for the current 
        # scenario.     
        for spot in available:  
            dummy_game.board[int(spot)] = self.letter
            score = self.minimax(self.letter, dummy_game, 0, False)
            # when we run the algo for one slot, return to the current state as we want to check all slots.
            dummy_game.board[int(spot)] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = spot
        game.board[int(bestMove)] = self.letter

    def minimax(self, player_letter, game_state, depth, isMaxPlayer):
        # we define the other player i.e minimum player w.r.t the computer letter
        other_player = 'X' if player_letter == 'O' else 'O'
        available = game_state.available_moves()
        # We have only 3 outcomes 1(max player wins), -1(min player wins), 0(Tie). This is a recursive function
        # and below 3 are base conditions
        if game_state.is_winner(player_letter):
            return 1
        elif game_state.is_winner(other_player):
            return -1
        # tie scenario
        if len(available) == 0:
            return 0

        # stimulationg the game with recursive condition as below and returning the best score
        if isMaxPlayer:
            bestScore = -inf    # worst score for a max player will be negative infinity
            for spot in available:
                game_state.board[int(spot)] = player_letter
                score = self.minimax(player_letter, game_state, depth + 1, False)
                bestScore = max(score, bestScore)
                game_state.board[int(spot)] = ' '
            return bestScore
        else:
            bestScore = inf    # worst score for a min player will be infinity
            for spot in available:
                game_state.board[int(spot)] = other_player
                score = self.minimax(player_letter, game_state, depth + 1, True)
                bestScore = min(score, bestScore)
                game_state.board[int(spot)] = ' '
            return bestScore
