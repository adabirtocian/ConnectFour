from computer import Computer
from exceptions_validators import BoardError


class Game:
    def __init__(self, board, computer_player):
        self._board = board
        self._computer_player = computer_player
        self._last_move_computer = (-1,-1)

    def get_board(self):
        return self._board

    def get_computer_player(self):
        return self._computer_player

    def get_last_move(self):
        return self._last_move_computer

    def get_winner_code(self):
        return self._board.get_winner_code()

    def move_player(self, column):
        '''
        Does the player move and raises an error if the move is invalid
        :param column: the column number
        '''
        line = self._board.find_empty_row_of_column(column)
        if line is not None:
            self._board.move(line, column, 1)
        else:
            raise BoardError("No empty positions")

    def move_computer(self):
        '''
        Does the computer move by calling the move method implemented for the computer player
        '''
        col_move = self._computer_player.move(self._board)
        row_move = self._board.find_empty_row_of_column(col_move)
        self._last_move_computer = (row_move, col_move)
        self._board.move(row_move, col_move, -1)

    def is_over(self):
        '''
        Checks whether the game is over
        :return: True for game over, False otherwise
        '''
        return self._board.is_won() or self._board.is_tie()