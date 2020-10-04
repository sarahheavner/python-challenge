#Import os module to create file path across operating systems
import os

#Import csv module to read CSV file
import csv


#Create path to CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

#Open csv file
with open(csvpath) as csvfile:
    #Set delimiter as comma
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip first row (header)
    csv_header = next(csvreader)

    total_votes = 0

    for row in csvreader:
        total_votes +=1

    print(total_votes)
        