import os
import glob
from time import time

sPath = 'C:\\Jagan\\temp'
# Loop through each object in the directory and get the file details and count of files and directories
for obj in glob.glob(os.path.join(sPath, '*')):
    print(f' File is {obj}, Filesize is {os.path.getsize(obj)}') 
    if os.path.isdir(obj):
        print(f'{obj} is directory')
    else:
        print(f'{obj} is file, Folder is {os.path.split(obj)[0]} and File is {os.path.split(obj)[1]}')

        
