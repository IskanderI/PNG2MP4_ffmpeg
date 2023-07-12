# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:21:41 2021

@author: iuralovi
"""
import os,shutil,sys,re,subprocess,time
from mpi4py import MPI
from dist import get_start_end
from pathlib import Path

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

def run( cmd):
    if sys.platform =='win32':
        result=subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
        print(result.stderr)
    else:
        os.system(cmd)


def split_folders(path):
    folders = []
    while 1:
        path, folder = os.path.split(path)
    
        if folder != "":
            folders.append(folder)
        elif path != "":
            folders.append(path)
    
            break      

    folders.reverse()
    return folders

# dirselect  = 'F:/Iskander/Lamem_models/2023/pics/tesmakevids/pics/'
# saveselect = "F:/Iskander/Lamem_models/2023/pics/tesmakevids/vids/"

dirselect  = sys.argv[1]
saveselect = sys.argv[2]

start_time   = time.time()
foldlist     = []
extensions   = ['.png','.jpeg','.jpg']
# Mark folders that contain pictures with extensions
for x in os.walk(dirselect):
    if not x[2]:        
         print("No png in " + x[0] ) 
    else :
        for png in extensions:
            if any(fname.endswith(png) for fname in os.listdir(x[0])):
                foldlist.append(x[0])

if not os.path.exists(saveselect):
    Path(saveselect).mkdir(parents=True, exist_ok=True)    

# MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
# range of models
startID = 0
numMods = len(foldlist)

# distribute workload among processors
rstart, rend = get_start_end(size, rank, numMods, startID)
partfoldlist = foldlist[rstart:rend]

#renaming files so they will go in order as file1 file2 file3 etc    

numfile=0

for files in partfoldlist:
    numfile += 1
    foldssplit = split_folders(files)
    idx=0
    print(f'Renaming files first {numfile}/{len(partfoldlist)}')
    for filename in natural_sort(os.listdir(files)):
        if filename.endswith('.png'):
            savename = foldssplit[-1] + foldssplit[-2]+ '_' +''.join([str(idx), '.png'])
            shutil.move(os.path.join(files, filename), os.path.join(files, savename))#os.path.join(root,''.join([str(idx), '.png'])))
            idx+=1
print("\n \n Time spent for renaming : --- %s seconds ---"  %(time.time() - start_time))
start_time   = time.time()

for fold in partfoldlist:
    idx=0
    for filename in natural_sort(os.listdir(fold)):
        
        if filename.endswith('.png'):
            break
        
    # Get file names and prepare format for ffmpeg command    
    splitname      = filename.split('_')
    splitname      = '_'.join(splitname[0:-1])
    allfilesname   = splitname +"_%01d"+".png"
    inputpicsname  = os.path.join(fold, allfilesname)
    
    # Create Names and folders for saving
    if fold == dirselect:
        savename       = splitname
        casefoldname   = saveselect
    else:
        casefoldname   = fold.replace(dirselect,'').strip(os.path.sep)
        savename       = casefoldname.replace(os.path.sep,'')
        
    savefold       = os.path.join(saveselect,casefoldname)
    
    if not os.path.exists(savefold):
        Path(savefold).mkdir(parents=True, exist_ok=True)
        
    gifname = os.path.join(savefold,savename+".mp4")
    #==============================
    cmd = "ffmpeg  -loop 0 -i " + inputpicsname + "  -c:v libx264 -pix_fmt yuv420p -vf \"scale=1920:1080  \" "+" "+gifname    #; ,split=2 [a][b],[a] palettegen [pal]; [b] fifo [b]; [b] [pal] paletteuse    
    run(cmd)
    idx+=1    
print("\n \n Time spent for calculation : --- %s seconds ---"  %(time.time() - start_time))