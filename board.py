from texttable import Texttable


class Board:
    def __init__(self):
        self._data = [[0] * 7, [0] * 7, [0] * 7, [0] * 7, [0] * 7, [0] * 7]
        self._moves = 0
        self._winner_code = 0

    def __str__(self):
        t = Texttable()
        for i in range(5, -1, -1):
            row = self._data[i][:]
            t.add_row(row)
        return t.draw()

    def get_board(self, x, y):
        return self._data[x][y]

    def get_moves(self):
        return self._moves

    def get_winner_code(self):
        return self._winner_code

    def find_empty_row_of_column(self, x):
        '''
        Returns the first empty space from the bottom of the board, on the x column
        :param x: column number
        :return: the line number for the empty space, None is there isn't an empty one
        '''
        for i in range(6):
            if self._data[i][x] == 0:
                return i
        return None

    def move(self, line, col, color_code):
        '''
        Simulates the move by marking the first empty position (from the bottom) on the x-th column with the color_code
        :param line: line number
        :param col: column number
        :param color_code: -1 for the computer and 1 for the player
        '''
        self._data[line][col] = color_code
        self._moves += 1

    def check_columns(self):
        '''
        Checks if the player has 4 of the same color on a column
        :return: True if there are 4 of the same color, False otherwise
        '''

        for col in range(7):
            for line in range(3):
                if self._data[line][col] == self._data[line+1][col] == self._data[line+2][col] == self._data[line+3][col] != 0:
                    self._winner_code = self._data[line][col]
                    return True
        return False

    def check_lines(self):
        '''
        Checks if the player has 4 of the same color on a line
        :return: True if there are 4 of the same color, False otherwise
        '''
        for line in range(6):
            for col in range(4):
                if self._data[line][col] == self._data[line][col+1] == self._data[line][col+2] == self._data[line][col+3] != 0:
                    self._winner_code = self._data[line][col]
                    return True
        return False

    def check_diagonals(self):
        '''
        Checks if the player has 4 of the same color on a diagonal
        :return: True if there are 4 of the same color, False otherwise
        '''
        # 4-diagonal
        if self._data[0][3] == self._data[1][2] == self._data[2][1] == self._data[3][0] != 0:  # secondary up
            self._winner_code = self._data[0][3]
            return True
        if self._data[2][6] == self._data[3][5] == self._data[4][4] == self._data[5][3] != 0:  # secondary down
            self._winner_code = self._data[2][6]
            return True
        if self._data[0][3] == self._data[1][4] == self._data[2][5] == self._data[3][6] != 0:  # primary up
            self._winner_code = self._data[0][3]
            return True
        if self._data[2][0] == self._data[3][1] == self._data[4][2] == self._data[5][3] != 0:  # primary down
            self._winner_code = self._data[2][0]
            return True

        # 5-diagonal
        if self._data[1][3] == self._data[2][2] == self._data[3][1] != 0 \
                and (self._data[1][3] == self._data[0][4] or self._data[1][3] == self._data[4][0]):  # secondary up
            self._winner_code = self._data[1][3]
            return True
        if self._data[2][5] == self._data[3][4] == self._data[4][3] != 0 \
                and (self._data[2][5] == self._data[1][6] or self._data[2][5] == self._data[5][2]):  # secondary down
            self._winner_code = self._data[2][5]
            return True
        if self._data[1][3] == self._data[2][4] == self._data[3][5] != 0 \
                and (self._data[1][3] == self._data[0][2] or self._data[1][3] == self._data[4][6]):  # primary up
            self._winner_code = self._data[1][3]
            return True
        if self._data[2][1] == self._data[3][2] == self._data[4][3] != 0 \
                and (self._data[2][1] == self._data[1][0] or self._data[2][1] == self._data[5][4]):  # primary down
            self._winner_code = self._data[2][1]
            return True

        # 6-diagonal
        if self._data[2][3] == self._data[3][2] != 0 and (self._data[2][3] == self._data[0][5] == self._data[1][4]
                                                          or self._data[2][3] == self._data[0][5] == self._data[4][1] or
                                                          self._data[2][3] == self._data[4][1] == self._data[5][
                                                              0]):  # secondary up
            self._winner_code = self._data[2][3]
            return True
        if self._data[2][4] == self._data[3][3] != 0 and (self._data[2][4] == self._data[0][6] == self._data[1][5]
                                                          or self._data[2][4] == self._data[1][5] == self._data[4][2] or
                                                          self._data[2][4] == self._data[4][2] == self._data[5][
                                                              1]):  # secondary down
            self._winner_code = self._data[2][4]
            return True
        if self._data[2][3] == self._data[3][4] != 0 and (self._data[2][3] == self._data[0][1] == self._data[1][2]
                                                          or self._data[2][3] == self._data[1][2] == self._data[4][5] or
                                                          self._data[2][3] == self._data[4][5] == self._data[5][
                                                              5]):  # primary up
            self._winner_code = self._data[2][3]
            return True
        if self._data[2][2] == self._data[3][3] != 0 and (self._data[2][2] == self._data[0][0] == self._data[1][1]
                                                          or self._data[2][2] == self._data[1][1] == self._data[4][4] or
                                                          self._data[2][2] == self._data[4][4] == self._data[5][
                                                              5]):  # primary down
            self._winner_code = self._data[2][2]
            return True

        return False

    def is_won(self):
        '''
        Check whether there is a horizontal, vertical, or diagonal line of four of one's own discs
        :return: True if the game was won
                 False otherwise
        '''

        return self.check_columns() or self.check_lines() or self.check_diagonals()

    def is_tie(self):
        '''
        Checks if the game ended with tie
        :return: True for tie, False otherwise
        '''
        return self._moves == 42 and not self.is_won()


