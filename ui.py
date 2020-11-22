from exceptions_validators import Validator as valid, BoardError


class Ui:
    def __init__(self, game):
        self._game = game

    def read_move(self):
        while True:
            try:
                coord = input("column = ")
                valid.coord_validate(coord)
                return int(coord)
            except ValueError:
                print("Column coordinate must be between 0 and 7")
            except TypeError:
                print("Wrong column !")

    def start(self):
        player_move = True
        while not self._game.is_over():
            if player_move:
                column = self.read_move()
                try:
                    self._game.move_player(column)
                    print(self._game.get_board(), "\n")
                except BoardError as e:
                    print(e)
            else:
                self._game.move_computer()
                print("Computer move:\n",self._game.get_board(), "\n")
            player_move = not player_move
        if self._game.is_over():
            if self._game.get_winner_code() == 1:
                print("You won !")
            else:
                print("The computer won !")





