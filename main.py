from computer import Computer
from game import Game
from ui import Ui
from board import Board
from gui import Gui

computer = Computer()
board = Board()
game = Game(board, computer)
ui = Ui(game)
gui = Gui(game)
gui.start()
