# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:54:29 2022

@author: iuralovi
!!!!! No spaces in directory names!!!!!!!!!

"""
import subprocess,os,time,sys
# Put the spaces before and after!
target = " C:/Users/iuralovi/.julia/conda/3/Scripts/activate.bat "
cmd    =  " mpiexec -n 6 python E:/iskander/lamemclass/scripts/makevids/makevids.py "

#======================================
"""
Import tk for file selection
to run with dialog windows in windows machines
# """
# if sys.platform =='win32':
#     from tkinter import filedialog as fd
#     from tkinter import Tk
#     win        = Tk()
#     ##ask in which folders it is necessary to take gifs
#     dirselect  = fd.askdirectory(title='Target folder')
#     saveselect = fd.askdirectory(title='Save video')
#     win.after_cancel(win)
#     win.after(1000,lambda:win.destroy())
#     win.mainloop()
# ===================================

# start_time = time.time()

dirselect  = 'F:/Iskander/Lamem_models/2023/pics/tesmakevids/pics/'
saveselect = "F:/Iskander/Lamem_models/2023/pics/tesmakevids/vids/"

def run( cmd):
    if sys.platform =='win32':
        result=subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
        print(result.stdout)
    else:
        os.system(cmd)

if sys.platform =='win32':
    run(target)
    run(cmd+dirselect+' '+saveselect)
else:
    os.system(cmd)

# time.sleep(2)
# print("\n \n Time spent for calculation : --- %s seconds ---"  %(time.time() - start_time))
  