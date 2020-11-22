import random


class Computer:
    def move(self, board):
        '''
        Does the computer's moves, taking into account the winning possibilities and the moves for blocking the player.
        In case there is no such move, a random choice will be made from the available moves
        :param board: the board
        :return: the column for the next move
        '''
        computer_moves = self.winning_possibility(board, -1)
        player_moves = self.winning_possibility(board, 1)
        one_connection_moves = self.one_connection(board)
        if not computer_moves:      # computer has no winning move
            if not player_moves:    # player has no winning move
                if not one_connection_moves:
                    possible_moves = self.generate_random_move(board)
                else:
                    possible_moves = one_connection_moves
            else:
                possible_moves = player_moves
        else:
            possible_moves = computer_moves
        return random.choice(possible_moves)

    def generate_random_move(self, board):
        '''
        Generates a list of all the possible moves that the computer can make
        :param board: the board
        :return: a list of columns' numbers, each being a possible move
        '''
        moves = []
        for col in range(7):
            row = board.find_empty_row_of_column(col)
            if row is not None:
                moves.append(col)
        return moves

    def winning_possibility(self, board, player_code):
        '''
        Check if the player has an opportunity to win and returns a list of possible moves to block him
        :param board: the board
        :param player_code: 1 for player, -1 for computer
        :return: a list of possible moves if any, empty list otherwise
        '''
        dx = [0, 0, 0, -1, -2, -3, -1, -2, -3, -1, -2, -3, 0, 0, 0]
        dy = [-1, -2, -3, -1, -2, -3, 0, 0, 0, 1, 2, 3, 1, 2, 3]
        possible_moves =[]
        for col in range(7):
            row = board.find_empty_row_of_column(col)
            if row is not None:
                for j in range(0, 13, 3):
                    new_row1 = row + dx[j]
                    new_col1 = col + dy[j]
                    new_row2 = row + dx[j+1]
                    new_col2 = col + dy[j+1]
                    new_row3 = row + dx[j+2]
                    new_col3 = col + dy[j+2]
                    if (0 <= new_row1 <= 5 and 0 <= new_col1 <= 5) and (0 <= new_row2 <= 5 and 0 <= new_col2 <= 5) and \
                        (0 <= new_row3 <= 5 and 0 <= new_col3 <= 5):
                        if board.get_board(new_row1, new_col1) == board.get_board(new_row2, new_col2) == player_code ==\
                                board.get_board(new_row3, new_col3) == player_code:
                            possible_moves.append(col)
        return possible_moves

    def one_connection(self, board):
        '''
        Checks the possibility of connecting 2 of computer_player's colour
        :param board: the board
        :return: a list of possible moves
        '''
        dx = [-1, -1, -1, 0, 0]
        dy = [-1, 0, 1, 1, -1]
        possible_moves = []
        for col in range(7):
            row = board.find_empty_row_of_column(col)
            if row is not None:
                for j in range(5):
                    new_row = row + dx[j]
                    new_col = col + dy[j]
                    if 0 <= new_row <= 5 and 0 <= new_col <= 5:
                        if board.get_board(new_row, new_col) == -1:
                            possible_moves.append(col)
        return possible_moves
