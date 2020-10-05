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

    #create lists to store data 
    candidate = []
    vote_count = []

    #set total votes variable to 0 
    total_votes = 0

    for row in csvreader:
        #create count for total votes
        total_votes = total_votes + 1

        #set variable for candidate name
        candidate_name = row[2]
        #Loop through rows to see if candidate name is in candidate list
        if candidate_name not in candidate:
            #add candidate name to candidate list
            candidate.append(candidate_name)
            #set initial voter count as 1
            vote_count.append(1)
        else:
            #create index reference for adding vote counts to correct candidate
            index = candidate.index(candidate_name)
            #add 1 vote for each time candidate name appears 
            vote_count[index] = vote_count[index] + 1
    
    #Find percentage votes per candidate
    percentage_vote0= round(float(vote_count[0])/total_votes * 100, 2)
    percentage_vote1= round(float(vote_count[1])/total_votes * 100, 2)
    percentage_vote2= round(float(vote_count[2])/total_votes * 100, 2)
    percentage_vote3= round(float(vote_count[3])/total_votes * 100, 2)

    #Determine winner by vote count
    winner = max(vote_count)
    winner_name = candidate[vote_count.index(winner)] 

    print('Election Results')
    print('---------------------------')
    print(f'Total Votes: {total_votes}')
    print('---------------------------')
    print(f'{candidate[0]}: {percentage_vote0}% {vote_count[0]}')
    print(f'{candidate[1]}: {percentage_vote1}% {vote_count[1]}')
    print(f'{candidate[2]}: {percentage_vote2}% {vote_count[2]}')
    print(f"{candidate[3]}: {percentage_vote3}% {vote_count[3]}")
    print('---------------------------')
    print(f'Winner: {winner_name}')
    print('---------------------------')


#Specify output path for txt file
output = os.path.join('Analysis', 'election_results.txt')

with open(output, 'w') as file:
    file.write('Election Results')
    file.write('\n')
    file.write('---------------------------')
    file.write('\n')
    file.write(f'Total Votes: {total_votes}')
    file.write('\n')
    file.write('---------------------------')
    file.write('\n')
    file.write(f'{candidate[0]}: {percentage_vote0}% {vote_count[0]}')
    file.write('\n')
    file.write(f'{candidate[1]}: {percentage_vote1}% {vote_count[1]}')
    file.write('\n')
    file.write(f'{candidate[2]}: {percentage_vote2}% {vote_count[2]}')
    file.write('\n')
    file.write(f"{candidate[3]}: {percentage_vote3}% {vote_count[3]}")
    file.write('\n')
    file.write('---------------------------')
    file.write('\n')
    file.write(f'Winner: {winner_name}')
    file.write('\n')
    file.write('---------------------------')



   



        

        

    
        