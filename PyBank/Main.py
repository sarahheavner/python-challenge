#Import os module to create file path across operating systems
import os

#Import csv module to read CSV file
import csv


#Create path to CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Open csv file
with open(csvpath) as csvfile:
    #Set delimiter as comma
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip first row (header)
    csv_header = next(csvreader)

    for row in csvreader:
        










