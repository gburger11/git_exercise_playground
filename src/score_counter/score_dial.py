from functools import partial
from pathlib import Path
import random
import tkinter as tk


NORMAL_INC = 1
BIG_INC = 5

FORMAT_NAME = "Verdana 15 bold"
FORMAT_SCORE = "Verdana 20"


class ScoreDial(tk.Frame):
    def __init__(self, master, name="", color="black"):
        super().__init__(master, relief=tk.RIDGE, borderwidth=3)

        tk.Label(master=self, text=name, font=FORMAT_NAME).grid(row=0, column=0, columnspan=4, sticky=tk.EW)

        # Add score
        self.current_score = tk.IntVar(master=self, value=0)
        tk.Label(master=self, textvariable=self.current_score, font=FORMAT_SCORE, fg=color).grid(row=1, column=0, columnspan=4, sticky=tk.EW)

        # Add buttons for updating the score
        tk.Button(master=self, text=f"-{BIG_INC}", command=partial(self.update_score, -BIG_INC)).grid(row=2, column=0)
        tk.Button(master=self, text=f"-{NORMAL_INC}", command=partial(self.update_score, -NORMAL_INC)).grid(row=2, column=1)
        tk.Button(master=self, text=f"+{NORMAL_INC}", command=partial(self.update_score, +NORMAL_INC)).grid(row=2, column=2)
        tk.Button(master=self, text=f"+{BIG_INC}", command=partial(self.update_score, +BIG_INC)).grid(row=2, column=3)

        # Add special double button
        self.magic_img = tk.PhotoImage(master=self, file=Path(__file__).parent / "images" / "magic.png")
        tk.Button(master=self, image=self.magic_img, text="+ rand", command=self.add_random, compound=tk.LEFT).grid(row=3, column=0, columnspan=4, sticky=tk.EW)

    def update_score(self, increment):
        self.current_score.set(self.current_score.get() + increment)

    def add_random(self):
        self.current_score.set(self.current_score.get() + random.randint(0, BIG_INC))
