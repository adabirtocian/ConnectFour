import tkinter as tk
from tkinter import *
from tkinter import messagebox


class Gui(Frame):
    def __init__(self, game):
        tk.Frame.__init__(self)
        self._game = game
        self._moves = [0, 0, 0, 0, 0, 0, 0]
        self._buttons = [[] * 7, [] * 7, [] * 7, [] * 7, [] * 7, [] * 7]

        self.pack()
        self.master.title("Connect 4")
        self.master.geometry("400x400")

        for i in range(6):
            for j in range(7):
                button = Button(self, height=2, width=5)
                button.grid(column=j, row=i)
                self._buttons[i].append(button)

        button0 = Button(self, bg="gray", text="0", height=2, width=5, command=lambda: self.on_click(0))
        button0.grid(column=0, row=6)
        button1 = Button(self, bg="gray", text="1", height=2, width=5, command=lambda: self.on_click(1))
        button1.grid(column=1, row=6)
        button2 = Button(self, bg="gray", text="2", height=2, width=5, command=lambda: self.on_click(2))
        button2.grid(column=2, row=6)
        button3 = Button(self, bg="gray", text="3", height=2, width=5, command=lambda: self.on_click(3))
        button3.grid(column=3, row=6)
        button4 = Button(self, bg="gray", text="4", height=2, width=5, command=lambda: self.on_click(4))
        button4.grid(column=4, row=6)
        button5 = Button(self, bg="gray", text="5", height=2, width=5, command=lambda: self.on_click(5))
        button5.grid(column=5, row=6)
        button6 = Button(self, bg="gray", text="6", height=2, width=5, command=lambda: self.on_click(6))
        button6.grid(column=6, row=6)

    def on_click(self, id_button):
        if self._moves[id_button] == 6:
            self.display_warning()
        else:
            # player moves
            self._game.move_player(id_button)
            self.mark_square(id_button)
            self._moves[id_button] += 1

            self.computer_play()
            print(self._game.get_board(), "\n")

    def mark_square(self, column):
        empty_square = self._moves[column]
        button = self._buttons[5-empty_square][column]
        if self._game.get_board().get_moves() % 2 == 0:
            button.configure(bg="red")
        else:
            button.configure(bg="yellow")

    def display_warning(self):
        messagebox.showinfo('Warning', 'The column is full !')

    def get_computer_move(self):
        last_move = self._game.get_last_move()
        return last_move[1]

    def game_finished(self):
        if self._game.get_winner_code() == 1:
            messagebox.showinfo('Game finished', 'You won!')
        elif self._game.get_winner_code() == -1:
            messagebox.showinfo('Game finished', 'The computer won !')

    def computer_play(self):
        if self._game.is_over():
            self.game_finished()
        else:
            # computer moves
            self._game.move_computer()
            id_button = self.get_computer_move()
            self.mark_square(id_button)
            self._moves[id_button] += 1
            if self._game.is_over():
                self.game_finished()
            print("Computer move:\n", self._game.get_board(), "\n")

    def start(self):
        self.mainloop()
