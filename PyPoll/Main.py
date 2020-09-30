#Import os module to allow files across different operating systems
import os

#Import module for reading csv files
import csv

#Create path to read csv file
csvpath = os.path.join("..", "Resources", "election_data.csv")


#Open csv file
with open(csvpath) as csv file:

    #Set csvreader with comma as delimiter
    csvreader = csv.reader(csvfile, delimiter=",")