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

    #Define Variables
    month_count = 0
    profit_loss=[]

    for row in csvreader:
        month_count += 1
        print(month_count)
        

        
        










