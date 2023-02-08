#9.	Write a function to delete files or directories.

import os
import shutil

def delete_file(directory):
    if (os.path.isfile(directory)):
        os.remove(directory)   
        print("Deleted file") 
    else:
        shutil.rmtree(directory)
        print("Deleted directory")

directory = input("Paste you filepath here: ")
# dir_or_file = input('Tell file name or folder : ')
delete_file(directory)