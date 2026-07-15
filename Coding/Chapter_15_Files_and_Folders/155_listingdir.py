import os
import time

sPath = 'C:\\Jagan\\temp'
sFile = 'C:\\Jagan\\temp\\Product.csv'

filedict = {'countofDirectory':0, 'countofFiles':0}

lst= []

# Loop through each object in the directory and get the file details and count of files and directories
for obj in os.listdir(sPath):
    filedate = os.path.getmtime(os.path.join(sPath, obj))
    mfiledate = time.ctime(filedate)
    ofiledate = time.strptime(mfiledate)
    tfiledate = time.strftime("%Y-%m-%d %H:%M:%S", ofiledate)
    print(f' File is {os.path.join(sPath, obj)}, Filesize is {os.path.getsize(os.path.join(sPath, obj))}, File modified date is {tfiledate}')

    if os.path.isdir(os.path.join(sPath, obj)):
        print(f'{os.path.join(sPath, obj)} is directory')
        filedict['countofDirectory'] = filedict['countofDirectory'] + 1
    else:
        print(f'{os.path.join(sPath, obj)} is file')
        filedict['countofFiles'] = filedict['countofFiles'] + 1
        filelist = list(os.path.splitext(os.path.join(sPath, obj)))
        if filelist[1] == ".csv":
            print(filelist[0],filelist[1])

print(f'The count of directories is {filedict['countofDirectory']}')
print(f'The count of directories is {filedict['countofFiles']}')
