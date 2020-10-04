#Import os module to create file path across operating systems
import os

#Import csv module to read CSV file
import csv


#Create path to CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Open csv file
with open(csvpath, newline='') as csvfile:
    #Set delimiter as comma
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip first row (header)
    csv_header = next(csvreader)

    #Define Variables
    date = []
    profit = []
    monthly_change = []

    #Set starting values at 0
    #month_count = 0
    #monthly_change = 0

    for row in csvreader:
        #Counts number of rows excluding header
        #month_count += 1
        #print(month_count)

        date.append(row[0])

        profit.append(int(row[1]))




    total_months=len(date)
    total_profit=sum(profit)

    print('Financial Analysis')
    print(f'----------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: {total_profit}')
   
    
        



        



        
        



        


        

        
        










