import tkinter as tk
from .score_dial import ScoreDial


class ScoreCounter(tk.Tk):
    """
    This class displays a simple score counter composed of several dials (one per player).
    """
    def __init__(self, n_player=2):
        super().__init__()

        # Create a dial for each player
        for player in range(n_player):
            ScoreDial(master=self, name=f"Player {player}").grid(row=0, column=player)

    def run(self):
        self.mainloop()
