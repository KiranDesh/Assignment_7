#4.	Write a function to read excel sheet file and display data on terminal.
import pandas as pd
 
def read_excel(filename):
    file = pd.read_excel(filename)
    print(file)
    # with open('excel_file.xlxs','w+') as f:
    #     f.write("Hello, world!")
    # f = open('excel_file.xlxs','r')
    # print(f.read())
filename = "file_example_XLSX_50.xlsx"
read_excel(filename)