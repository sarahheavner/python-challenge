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
    total_months = len(date)
    #Calculate total profit
    total_profit = sum(profit)
    #Calculate average montly change
    total_monthly_change = sum(monthly_change)
    average_change = round((total_monthly_change)/(int(total_months)-1),2)
    #Identify greatest monthly increase and decrease
    greatest_increase = max(monthly_change)    
    greatest_decrease = min(monthly_change)
    #Identify date of greatest monthly increase and decrease referencing list index
    month_inc = date[monthly_change.index(greatest_increase)]
    month_dec = date[monthly_change.index(greatest_decrease)]
    
    #print financial analysis
    print('Financial Analysis')
    print(f'----------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: {total_profit}')
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profits: {month_inc} ({greatest_increase})')
    print(f'Greatest Decrease in Profits: {month_dec} ({greatest_decrease})')


#Specify output path for txt file
output = os.path.join('Analysis', 'pybank_analysis.txt')
#open as txtfile writer
with open(output, 'w') as file:
    #Write results to txt file
    file.write('Financial Analysis')
    file.write('\n')
    file.write(f'----------------------')
    file.write('\n')
    file.write(f'Total Months: {total_months}')
    file.write('\n')
    file.write(f'Total: {total_profit}')
    file.write('\n')
    file.write(f'Average Change: {average_change}')
    file.write('\n')
    file.write(f'Greatest Increase in Profits: {month_inc} ({greatest_increase})')
    file.write('\n')
    file.write(f'Greatest Decrease in Profits: {month_dec} ({greatest_decrease})')

   



        



        
        



        


        

        
        










