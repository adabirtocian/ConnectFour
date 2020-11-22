import unittest
from board import Board
from computer import Computer
from exceptions_validators import BoardError
from game import Game


class TestBoard(unittest.TestCase):
    def test_no_winner(self):
        b = Board()
        b.move(0, 2, 1)
        b.move(1, 2, -1)
        b.move(2, 2, 1)

        self.assertEqual(b.is_won(), False)    # no winner
        self.assertEqual(b.is_won(), False)
        self.assertEqual(b.get_winner_code(), 0)

    def test_winner_column(self):
        b = Board()
        b.move(0, 3, 1)
        b.move(1, 3, 1)
        b.move(2, 3, 1)
        b.move(3, 3, 1)
        b.move(4, 3, -1)

        self.assertEqual(b.find_empty_row_of_column(3), 5)

        self.assertEqual(b.check_columns(), True)   # won on the column
        self.assertEqual(b.is_won(), True)
        self.assertEqual(b.get_winner_code(), 1)

    def test_winner_line(self):
        b = Board()
        b.move(0, 0, -1)
        b.move(0, 1, -1)
        b.move(0, 2, -1)
        b.move(0, 3, -1)
        self.assertEqual(b.check_lines(), True)  # won on the line
        self.assertEqual(b.is_won(), True)
        self.assertEqual(b.get_winner_code(), -1)

    def test_winner_diagonal(self):
        b = Board()
        b.move(0, 0, 1)
        b.move(1, 0, 1)

        b.move(0, 1, 1)
        b.move(1, 1, 1)
        b.move(2, 1, 1)

        b.move(0, 2, 1)
        b.move(1, 2, 1)
        b.move(2, 2, 1)
        b.move(3, 2, 1)

        b.move(0, 3, 1)
        b.move(1, 3, 1)
        b.move(2, 3, 1)
        b.move(3, 3, 1)
        b.move(4, 3, 1)
        b.move(5, 3, 1)
        self.assertEqual(b.check_diagonals(), True) # won on diagonal
        self.assertEqual(b.is_won(), True)

        b1 = Board()
        b1.move(0, 0, 1)
        b1.move(1, 0, 1)
        b1.move(2, 0, 1)
        b1.move(3, 0, 1)

        b1.move(0, 1, 1)
        b1.move(1, 1, 1)
        b1.move(2, 1, 1)

        b1.move(0, 2, 1)
        b1.move(1, 2, 1)

        b1.move(0, 3, 1)
        self.assertEqual(b1.check_diagonals(), True)  # won on diagonal


class TestGame(unittest.TestCase):
    def test_move_player(self):
        c = Computer()
        b = Board()
        g = Game(b,c)
        b.move(0, 3, 1)
        b.move(1, 3, 1)
        b.move(2, 3, 1)
        b.move(3, 3, 1)
        b.move(4, 3, 1)
        b.move(5, 3, 1)
        with self.assertRaises(BoardError):     # column is full
            g.move_player(3)
        g.move_player(0)
        self.assertEqual(g.get_board().get_board(0,0), 1)

    def test_is_over(self):
        c = Computer()
        b = Board()
        g = Game(b, c)
        b.move(0, 3, 1)
        b.move(1, 3, 1)
        b.move(2, 3, 1)
        b.move(3, 3, 1)
        self.assertEqual(g.is_over(), True)


class TestComputer(unittest.TestCase):
    def test_computer(self):
        c = Computer()
        b = Board()
        g = Game(b, c)

        b.move(0, 1, -1)
        b.move(0, 2, -1)
        b.move(0, 3, -1)
        b.move(1, 2, 1)
        b.move(2, 2, 1)
        g.move_computer()
        self.assertEqual(b.is_won(), True)

    def test_winning(self):
        c = Computer()
        b = Board()
        g = Game(b, c)

        b.move(0, 0, -1)
        b.move(1, 0, -1)
        b.move(2, 0, -1)
        self.assertEqual(len(c.winning_possibility(b,-1)), 1)

        b.move(0, 2, 1)
        b.move(0, 3, 1)
        b.move(0, 4, -1)
        self.assertEqual(len(c.one_connection(b)), 5)



