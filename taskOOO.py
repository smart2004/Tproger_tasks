import os
from os import listdir
from os.path import isfile, join

directory_path = 'D:/smart2004/'
all_files = os.listdir(directory_path)

files = []

for f in all_files:
    if os.path.isfile(os.path.join(directory_path, f)):
        files.append(f)

print(files)
