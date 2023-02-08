#7.	Write a function to create CSV file with content.
import pandas as pd

# def create_csv_file(input_7):
#     with open("create_csv.csv", "a+") as f:
#         f.write(input_7+'\n')
        
# input_7 = input("Enter text comma sepearted ")
# create_csv_file(input_7)

d1 = {'Name': ['Pankaj', 'Meghna'], 'ID': [1, 2], 'Role': ['CEO', 'CTO']}
df = pd.DataFrame(d1)
df.to_csv("create_csv.csv")