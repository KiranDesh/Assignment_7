#5.	Write a function to read csv file and display data on terminal.
import pandas as pd

def read_csv(file):
    csv = pd.read_csv(file)
    print(csv)
    # with open(file) as f:
    #     print(f.read())
       
file = 'monthly_temperature.csv'
read_csv(file)
