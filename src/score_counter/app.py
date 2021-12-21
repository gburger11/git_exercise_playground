import tkinter as tk
from .score_dial import ScoreDial


COLORS = ["red", "blue", "green"]


class ScoreCounter(tk.Tk):
    def __init__(self, n_player=2):
        super().__init__()

        # Create a dial for each player
        for player, color in enumerate(COLORS):
            ScoreDial(master=self, name=f"Player {player}", color=color).grid(row=0, column=player)

    def run(self):
        self.mainloop()
