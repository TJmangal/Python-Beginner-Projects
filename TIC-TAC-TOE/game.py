win_list = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]


class Game:

    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_current_board(self):
        lst = [self.board[i*3: (i+1)*3] for i in range(3)]
        for row in lst:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_with_numbers():
        lst = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in lst:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        lst = [str(slot) for slot, letter in enumerate(self.board) if letter == " "]
        return lst

    def is_winner(self, letter):
        for win in win_list:
            for slot in win:
                if self.board[slot] != letter:
                    break
            else:
                return True
        return False
