import os
import time

sPath = 'C:\\Jagan\\temp'
sFile = 'C:\\Jagan\\temp\\Product.csv'

for root, dirs, files in os.walk(sPath, topdown=True):
    print(f'Directory path: {root}')
    print(f'Subdirectories: {dirs}')
    print(f'Files: {files}')
