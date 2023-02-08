#13.	Write a function to display content of directory.

import os

def display_directory(directory):
    print(os.listdir(directory))
    
directory = input("Enter directory path: ")
display_directory(directory)
    