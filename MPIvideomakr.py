# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:54:29 2022

@author: iuralovi
!!!!! No spaces in directory names!!!!!!!!!

"""
import subprocess,os,time,sys
import argparse

#======================================
"""
Import tk for file selection
to run with dialog windows in windows machines
# """
parser = argparse.ArgumentParser()
parser.add_argument("ncores", help="Amount of cores",type=str)
if sys.platform =='win32':
    args       = parser.parse_args()
    from tkinter import filedialog as fd
    from tkinter import Tk
    win        = Tk()
     ##ask in which folders it is necessary to take gifs
    dirselect  = fd.askdirectory(title='Target folder')
    saveselect = fd.askdirectory(title='Save video')
    win.after_cancel(win)
    win.after(1000,lambda:win.destroy())
    win.mainloop()
else:

    parser.add_argument("Folder", help="Folder of the images",type=str)
    parser.add_argument("ptsave",help="Folder where to put the output",type=str)
    args       = parser.parse_args()
    dirselect  = args.Folder
    saveselect = args.ptsave
ncores     = args.ncores

# ===================================

# Put the spaces before and after!
cmd    =  " mpiexec -n " + ncores +" python " + sys.path[0] + "/__main__.py "
os.system(cmd  + dirselect + ' ' + saveselect ) 
