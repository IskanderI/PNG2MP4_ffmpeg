# PNG2MP4_ffmpeg
This python script converts image folders to .mp4 videos. 

Thanks to great compressibility options your data can be stored in a more compressed way! :shipit:
#### Script based on:
  - 1. ffmpeg encoder to create videos which means high efficiency.
  - 2. MPI library to parallelise a task for multiple folders.
## How to Install
### Windows
#### (minimal)


#### (easy)
1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
> bash ./Miniconda3-py38_23.5.0-3-Linux-x86_64.sh

>  conda activate
2. Install MPI4py
> pip install mpi4py 
3. Install ffmpeg
>   conda deactivate

>   sudo apt instalacl ffmpeg
## How to Use
##### For Unix (Linux) sustems
To start a script, run from preferred command line, see next example:

> python3 /mnt/path_to_script/PNG2MP4_ffmpeg/MPIvideomakr.py  6 /mnt/path_to_target/pics/ /mnt/path_to_save/vids/

Where 6 in this example shows amount of cores that will be used by script.

##### For windows:
Start a script with 
> python3 /mnt/path_to_script/PNG2MP4_ffmpeg/MPIvideomakr.py 6

Then an interactive window will suggest to choose a folder with tests with images.

Second interactive window will ask for folder where to save videos.


> **Note**
>##  Warning! For correct working of script all images will be renamed!!
