# python-challenge

    challenge was to create new repository in github with a folder for each pybank and pypoll
        created repository 
        cloned to set file path on local computer through gitbash
            opened Visual Studio Code 
            created new folder for pybank and pypoll
                created main.py file within each folder
                created Resources and Analysis folder subfolders within pybank and pypoll main folders
                    located .csv files in repositories pulled from gitlab assignments
                        saved copy of .csv file in designated Resource folder to be able to create file path to read .csv for each assignment
                


## pybank-challenge
    challenge was to import csv file, read and analyze data, and have outputs print in terminal and create a txt file
        created .csv file path to read file from Resource folder
        opened .csv file to reader
        skipped header 
        created list designations
        set initial previous revenue as profit value of first row
            used this value becuase the first row would not have a "previous revenue" to calculate
        created loop to add values to each list per row
            appended date and profit lists 
            appended monthly change list
                calculated monthly change by subtracting current row profit - previous row profit
            reset current row profit for next row calculation
        counted number of months by using len of date rows
        calculated total profit as sum of rows of profit
        calculated total monthly change as sum of monthly change
            calculated average change by taking total monthly change divided by number of months (subtracted 1 month since first row does not have monthly change value)
        calculated greatest increase and greatest decrease by using min and max of monthly change
        used index of greatest increase and greatest decrease to find corresponding month
    added print statements to show results in terminal
    created output file path for txt file to save to Analysis folder
    wrote results into txt file


## pypoll-challenge
    challenge was to import csv file, read and analyze data, and have outputs print in terminal and create a txt file
        created .csv file path to read file from Resource folder
        opened .csv file to reader
        skipped header 
        created list designations
        created loop 
            if statement to find unique candidate names
                every time new candidate name appears, appended name to be added to candidate list
                set initial vote count as 1
                for every time candidate name appeared in row after name added to candidate list, added 1 vote to the proper index in vote count list
        calculated % of total votes for every index value in vote count list
        found winner by taking max value of vote count list
    added print statements to show results in terminal
    created output file path for txt file to save to Analysis folder
    wrote results into txt file

pushed all finished work to github 
submitted github link to bootcampspot for grading



        


