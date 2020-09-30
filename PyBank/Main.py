#Import os module to allow files across different operating systems
import os

#Import module for reading csv files
import csv

#Create path to read csv file
pybank_csv = os.path.join("..", "Resources", "budget_data.csv")


#Open csv file
with open(pybank_csv) as csvfile:

    #Set csvreader with comma as delimiter
    csvreader = csv.reader(csvfile, delimiter=",")

