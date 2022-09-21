import tkinter as tk
from .score_dial import ScoreDial


PLAYERS = ["pierre", "paul", "jacques"]
COLORS = ["pink", "cyan", "orange"]


class ScoreCounter(tk.Tk):
    def __init__(self, n_player=2):
        super().__init__()
        print("coucou !!")

        # Create a dial for each player
        for idx, (player, color) in enumerate(zip(PLAYERS, COLORS)):
            ScoreDial(master=self, name=player, color=color).grid(row=0, column=idx)

    def run(self):
        self.mainloop()
