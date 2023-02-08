#10.	Write a function where its file or directory.
 
import os

def file_directory_exists(filename):
    print(os.path.exists(filename))
    
filename = input("Enter the file name or paste directory: ")
file_directory_exists(filename)
    
    