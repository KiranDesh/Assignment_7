# 11.	Write a function to copy data from one directory to another directory.

import os
import shutil
def copy_directory(path1, path2):
    print(shutil.copytree(path1, path2))

path1  = input("Enter a path you want to copy from : ")
path2 = input("Enter a path you want to paste into : ")
copy_directory(path1, path2)