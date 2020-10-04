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

    #Create Lists
    date = []
    profit = []
    monthly_change = []

    #Set previous_revenue value as first profit/loss value in data set
    previous_revenue = 867884
    
    #Loop through and append lists
    for row in csvreader:
        #Append lists through loop
        date.append(row[0])
        profit.append(int(row[1]))
        #Calculate monthly change in revenue
        monthly_change.append(int(row[1]) - previous_revenue)
        #Reset previous_revenue value for next loop calculation
        previous_revenue = int(row[1])

        
    #Count number of rows 
    total_months=len(date)
    #Calculate total profit
    total_profit=sum(profit)
    #Calculate average montly change
    total_monthly_change = sum(monthly_change)
    average_change=round((total_monthly_change)/(int(total_months)-1),2)
    #Identify greatest monthly increase and decrease
    greatest_increase=max(monthly_change)    
    greatest_decrease=min(monthly_change)
    
    #print financial analysis
    print('Financial Analysis')
    print(f'----------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: {total_profit}')
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase}')
    print(f'Greatest Decrease in Profits: {greatest_decrease}')
   
    
        



        



        
        



        


        

        
        










