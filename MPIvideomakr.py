# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:54:29 2022

@author: iuralovi
!!!!! No spaces in directory names!!!!!!!!!

"""
import subprocess,os,time,sys

def run(cmd): # for windows through powershell
    result=subprocess.run(["powershell", "-Command Invoke-Expression ", cmd], capture_output=True, text=True)
    print(result.stdout)
#======================================
"""
Import tk for file selection
to run with dialog windows in windows machines
# """
if sys.platform =='win32':
    ncores = 6
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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("ncores", help="Amount of cores",type=int)
    parser.add_argument("Folder", help="Folder of the images",type=str)
    parser.add_argument("ptsave",help="Folder where to put the output",type=str)
    args       = parser.parse_args()
    dirselect  = args.Folder
    saveselect = args.ptsave
    ncores     = args.ncores

# ===================================

# Put the spaces before and after!
target = " C:/Users/$($Env:UserName)/.julia/conda/3/Scripts/activate.bat "
cmd    =  " mpiexec -n " + ncores +" python3 " + sys.path[0] + "/makevids.py "

if sys.platform =='win32':
    run(target)
    run(cmd+dirselect+' '+saveselect)
else:
    os.system(cmd  + dirselect + ' ' + saveselect ) 
