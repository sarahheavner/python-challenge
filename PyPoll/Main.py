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

    candidate_dict = {"name" : [], "vote_percentage" : [], "vote_count": []}

    vote_count = 0
    total_votes = 0

    for row in csvreader:
        total_votes = total_votes + 1
    



    print('Election Results')
    print('---------------------------')
    print(f'Total Votes: {total_votes}')
    print('---------------------------')
    #print(f'Kahn: {khan_percentage}%  {vote_count}')
    #print(f'Correy: {correy_percentage}%  {vote_count}')
    #print(f'Li: {li_percentage}, {vote_count}')
    #print(f"O'Tooley: {otooley_percentage}, {vote_count}")
    #print('---------------------------')
    #print(f'Winner: {most_votes}')
    #print('---------------------------')

        

    
        