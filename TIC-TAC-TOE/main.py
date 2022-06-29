import player
import game
import time

def choose_player():
    while True:
        player1 = player.HumanPlayer()
        player2_choise = input("Enter Y is you want to play against a friend and N to play against the computer: ").upper()
        if player2_choise in ['Y', 'N']:
            if player2_choise == 'Y':
                player2 = player.HumanPlayer()
            else:        
                player2 = player.ComputerPlayer(player1.letter)
            break
        else:
            print("Invalid Choise!!")
    return player1, player2


if __name__ == "__main__":
    player1, player2 = choose_player()
    game = game.Game()
    game.print_board_with_numbers()
    is_player1_winner, is_player2_winner = False, False
    print("Let's Begin... \n")

    while len(game.available_moves()) != 0:

        print("Choose your spot.")
        print("you have following slots remaining - " + " ".join(game.available_moves()))

        print("Player1's Turn...")
        time.sleep(2)
        player1.choose_slot(game)
        game.print_current_board()
        is_player1_winner = game.is_winner(player1.letter)
        if is_player1_winner is True:
            print("Player1 Wins!")
            break

        print("Player2's Turn...")
        time.sleep(2)
        player2.choose_slot(game)
        game.print_current_board()
        is_player2_winner = game.is_winner(player2.letter)
        if is_player2_winner is True:
            print("Player2 wins!")
            break

    if is_player1_winner is False and is_player2_winner is False:
        print("It's a Tie")
