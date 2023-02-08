#1.	Write a function to create simple text file with some text content.


def create_simple_text(input_1):
    with open('create_file.txt', 'a+') as f:
        f.write(input_1+"\n")
    
input_1 = input("Enter any text : ")
create_simple_text(input_1)