import random


class TicTacToe:
    def __init__(self, field_size):
        self.game_field = [[j + i * field_size for j in range(1, field_size + 1)] for i in range(0, field_size)]
        self.turn_counter = 0

    def show_game_field(self):
        for row in self.game_field:
            print("\n" + "-----" * len(self.game_field) + "---" * (len(self.game_field) - 1))
            for component in row:
                print("|", component, "|", end='\t')
        else:
            print("\n" + "-----" * len(self.game_field) + "---" * (len(self.game_field) - 1))

    def play(self, number, sign):
        for i in range(len(self.game_field)):
            for j in range(len(self.game_field[i])):
                if (i * len(self.game_field[i]) + j + 1 == number) and (self.game_field[i][j] == number):
                    self.game_field[i][j] = sign
                    return
        else:
            print(f"Invalid number! ({number})")
            raise ValueError

    def if_game_is_over(self):
        row_list = [i for i in self.game_field]
        column_list = [[self.game_field[j][i] for j in range(len(self.game_field))] for i in range(len(self.game_field))]
        first_diagonal = [self.game_field[i][j] for i in range(len(self.game_field)) for j in range(len(self.game_field)) if i == j]
        second_diagonal = [self.game_field[i][j] for i in range(len(self.game_field)) for j in range(len(self.game_field)) if j == len(self.game_field) - i - 1]

        if row_list.__contains__(['X'] * len(self.game_field)) or column_list.__contains__(['X'] * len(self.game_field)) or first_diagonal == ['X'] * len(self.game_field) or second_diagonal == ['X'] * len(self.game_field):
            print("The winner is 'X'")
            return True
        elif row_list.__contains__(['O'] * len(self.game_field)) or column_list.__contains__(['O'] * len(self.game_field)) or first_diagonal == ['O'] * len(self.game_field) or second_diagonal == ['O'] * len(self.game_field):
            print("The winner is 'O'")
            return True
        else:
            return False


def integer_input_validation(text):
    while True:
        try:
            integer_input = int(input(text))
            return integer_input
        except ValueError:
            continue


def start_game():
    selected_size = 0
    while selected_size < 3 or selected_size > 9:
        selected_size = integer_input_validation("Choose game field size [3-9]: ")
    return TicTacToe(selected_size)


def main():
    game = start_game()
    options = ['X', 'O']
    first_sign_index = random.randint(0, 1)
    while not game.if_game_is_over():
        game.show_game_field()
        print(f"It's '{options[(game.turn_counter + first_sign_index) % 2]}' turn!")
        try:
            game.play(integer_input_validation("Choose number: "), options[(game.turn_counter + first_sign_index) % 2])
        except ValueError:
            continue

        game.turn_counter += 1
        print("=" * 80)
    else:
        game.show_game_field()
        print(f"Game is over after {game.turn_counter} turns")


main()
