#2.	Write a function to read an existing text file and display its contents in terminal

def read_existing_file():
    with open("create_file.txt", "r") as f:
        print(f.read())

read_existing_file()