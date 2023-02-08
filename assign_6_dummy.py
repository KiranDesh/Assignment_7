#8.	Write a function to generate dummy files? Create large dummy / test files / directories with data size 1 to 10 GB. ( Do require internet research )

import os
size = 1073741824 # bytes in 1 GiB
def dummy_file_create(filename,size_given):
    with open(filename,'wb') as f:
        # f.write(size_given*size)
        print("Size of file : ",f.write(os.urandom(size_given*size)))# os.urandom() function  will genrate the random data
        print("Size of file : ",os.path.getsize(filename))
filename = input("Enter a filename you want to create : ")
size_given = int(input("Size of the file you want to create : "))
dummy_file_create(filename,size_given)