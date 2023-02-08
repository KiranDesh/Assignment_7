#14.	Write a function to change permission of file or directories.

import os
import stat

def change_permissions(filename,permission):
    os.chmod(filename,permission)
    print("file permission changed to: ",permission)
    
filename = input("Enter a file path here: ")
permission = int(input("Enter a permission like (stat.S_IREAD or stat.S_IWRITE): "))

change_permissions(filename,permission)