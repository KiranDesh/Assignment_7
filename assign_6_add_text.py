#3.	Write a function to add text content to any existing file.


def add_text(input_3):
    with open("create_file.txt", "a+") as f:
        f.write(input_3+'\n')
    
input_3 = input("Enter a text add : ")
add_text(input_3)