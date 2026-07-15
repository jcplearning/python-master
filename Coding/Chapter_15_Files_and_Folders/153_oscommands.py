import os
import time

sPath = 'C:\\Jagan\\temp'
sFile = 'C:\\Jagan\\temp\\Product.csv'

# Get the current working directory
print(os.getcwd())

# Check if the path is directory or file 
print(os.path.isdir(sPath))
print(os.path.isfile(sFile))

# change the current working directory and list the files in the directory
#os.chdir("Scripts")
#print(os.getcwd())
print(os.listdir(sPath))
print(os.path.exists(sPath))


