#!/usr/bin/env python3
from datetime import date
from escpos import config
from mock import *
from mocksources import *

import httpx

#c = MockConfig() # noqa: ERA
c = config.Config()
p = c.printer()

def morning_header():
    p.set_with_default(
        align="center",
        double_height=True,
        double_width=True,
        bold=True,
        underline=True,
        )

    p.textln(f"\n\n{date.today()}")
    p.set_with_default()


def todo_list():
    p.set_with_default(bold=True, underline=True)
    p.textln('\nTODO\n')
    p.set_with_default()
    for i in fetch_todos():
      p.textln(f"[ ] {i}")

    p.textln('\nBONUS GOALS\n')
    bonus = bonus_goals()[0]
    p.textln(f"[ ] {bonus}")
    p.set_with_default()

def whimsy():
    # add some whimsical stuff here

    #ideas:
    #cowsay
    # fortunes
    # quotes
    # sudoku
    # mazes
    # images/memes
    # etc
    pass


def morning_brief():
    morning_header()
    coin_price()
    #news_events()
    todo_list()
    #concert_tonight()
    #whimsy()

    # a few extra blank lines
    p.ln()
    p.ln()


if __name__=="__main__":
    morning_brief()


