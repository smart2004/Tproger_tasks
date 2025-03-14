from os import listdir
from os.path import isfile, join
files = [f for f in listdir('D:/smart2004/') if isfile(join('D:/smart2004/', f))]
print(files)
