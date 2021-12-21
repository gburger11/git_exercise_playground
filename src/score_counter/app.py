import tkinter as tk
from .score_dial import ScoreDial


class ScoreCounter(tk.Tk):
    def __init__(self, n_player=2):
        super().__init__()

        # Create a dial for each player
        for player in range(n_player):
            ScoreDial(master=self).grid(row=0, column=player)

    def run(self):
        self.mainloop()
