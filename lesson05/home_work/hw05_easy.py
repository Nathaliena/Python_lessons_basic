# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


try:
    for i in range(1,3):
        os.mkdir("dir_" + str(i))
except:
    print("Done")

try:
    for i in range(1,3):
        os.rmdir("dir_" + str(i))
except:
    print("Removed")





# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import sys

print("sys.path= ",sys.path)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

shutil.copy('гик_5.py','гик_5_copy.py')


