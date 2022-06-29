import random
winsByUser = 0
winsByComputer = 0
lst = ["rock", "paper", "scissors"]
noOfGames = 10


def game_logic(user_input: str, computer_input: str):
    """ :param user_input: string
        :param computer_input: string
        :return: Integer
        returns number of wins of user or computer while playing snake, water & gun game
    """
    global winsByUser
    global winsByComputer
    global noOfGames

    if (user_input == "paper" and computer_input == "rock") or (user_input == "rock" and computer_input == "scissors") \
            or (user_input == "scissors" and computer_input == "paper"):
        winsByUser += 1
    elif user_input == computer_input:
        print("It's a draw")
    else:
        winsByComputer += 1
    print(f"Wins by computer = {winsByComputer}, Wins by user = {winsByUser}\n")

    if noOfGames == 0:
        if winsByUser > winsByComputer:
            print("User Wins")
        elif winsByUser == winsByComputer:
            print("It's a draw")
        else:
            print("Computer wins")


if __name__ == "__main__":

    while noOfGames >= 1:

        user_choice = input("Enter rock, paper or scissors: ")
        if user_choice not in lst:
            print("invalid Choice!!!\n")
            continue

        computer_choice = random.choice(lst)
        print(f"computer chooses {computer_choice}")

        noOfGames -= 1
        game_logic(user_choice.lower().strip(), computer_choice)



