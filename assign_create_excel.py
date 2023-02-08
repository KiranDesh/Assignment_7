#6.	Write a function to create a excel sheet file with content.
import pandas as pd
# def create_excel(input_6):
#     with open('new_xlxs', 'w') as f:
#         f.write(input_6)
        
# input_6 = input("Enter a text : ") 
# create_excel(input_6)
    
d1 = {'Name': ['Pankaj', 'Meghna'], 'ID': [1, 2], 'Role': ['CEO', 'CTO']}
df = pd.DataFrame(d1)
df.to_excel('new_xlsx.xlsx')
