#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     mb_om_demo_support.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #197
# Written by G.D. Walters
# Copyright (c) 2023 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Aug 31, 2023 06:12:25 AM CDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import mb_om_demo

_debug = True  # False to eliminate debug printing from callback functions.


def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = mb_om_demo.Toplevel1(_top1)
    startup()
    root.mainloop()


def startup():
    setup_menubutton_items()
    setup_optionmenu_items()
    create_menubutton()
    create_optionmenu()


def menubutton_callback(*args):
    global carTypes, selection
    which = selection.get()
    print(f"Menubutton returned {carTypes[which]}")
    _w1.mbReturnValue.set(carTypes[which])


def optionmenu_callback(*args):
    global returnval
    which = returnval.get()
    print(f"OptionMenu returned {which}")
    _w1.omReturnValue.set(which)


def create_menubutton():
    global carTypes
    global selection
    # Set the container frame to flat relief
    _w1.mbFrame.configure(relief="flat")
    selection = tk.IntVar()
    mnuBtn = ttk.Menubutton(_w1.mbFrame, text="Items")
    mnuBtn.pack(expand=True, side="top", fill="both", anchor="nw")
    mnuBtn.menu = tk.Menu(mnuBtn, disabledforeground="black", tearoff=0)
    mnuBtn["menu"] = mnuBtn.menu
    cntr = 0
    for car in carTypes:
        mnuBtn.menu.add_radiobutton(
            label=car, command=menubutton_callback, value=cntr, variable=selection
        )
        cntr += 1


def create_optionmenu():
    global optionlist
    global returnval
    # Set the container frame to flat relief
    _w1.omFrame.configure(relief="flat")
    returnval = tk.StringVar()
    returnval.set("Options")
    optMenu = ttk.OptionMenu(
        _w1.omFrame, returnval, None, *optionlist, command=optionmenu_callback
    )
    optMenu.pack(expand=True, side="top", fill="both", anchor="nw")


def setup_menubutton_items():
    global carTypes
    carTypes = ["Chevy", "Oldsmobile", "Chrysler", "Jeep", "Toyota"]


def setup_optionmenu_items():
    global optionlist
    optionlist = ("Red", "Orange", "Yellow", "Green", "Blue", "Violet")


def on_btnExit(*args):
    if _debug:
        print("mb_om_demo_support.on_btnExit")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    sys.exit()


if __name__ == "__main__":
    mb_om_demo.start_up()
