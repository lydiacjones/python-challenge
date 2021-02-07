#PyBank

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#import dependencies
import os
import csv

#open csv and read
csvpath = os.path.join('Resources', 'Homework_03-Python_PyBank_Resources_budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #initialize variables and list
    months = 0
    total_net = 0
    diff = 0
    avg_change = 0
    previous = None
    monthly_diff = {}

    # Read and print header
    csv_header = next(csvreader)

    # for loop to add months, add net profits, calculate monthly diff and create list, and set previous row
    for row in csvreader:
        
        months += 1
        total_net += int(row[1])
        if previous != None:
            diff = int(row[1]) - previous
            monthly_diff[row[0]] = diff
        previous = int(row[1])
    
    #calculations
    max_increase = max(monthly_diff, key=monthly_diff.get) 
    max_decrease = min(monthly_diff, key=monthly_diff.get)
    avg_change = sum(monthly_diff.values()) / len(monthly_diff.values())

    #print to terminal
    print('Financial Analysis')
    print('----------------------------------')
    print(f'Total Months  : {months}')
    print(f'Net Total Profits/Losses : ${total_net}')
    print(f'Average Change : ${avg_change:.2f}')
    print(f'Greatest Increase in Profits : {max_increase} (${monthly_diff[max_increase]})')
    print(f'Greatest Decrease in Profits : {max_decrease} (${monthly_diff[max_decrease]})')

#print to text file
PyBank = open('Analysis/PyBank.txt', 'w')

PyBank.write('Financial Analysis\n')
PyBank.write('----------------------------------\n')
PyBank.write(f'Total Months  = {months}\n')
PyBank.write(f'Net Total Profits/Losses = ${total_net}\n')
PyBank.write(f'Average Change = ${avg_change:.2f}\n')
PyBank.write(f'Greatest Increase in Profits : {max_increase} (${monthly_diff[max_increase]})\n')
PyBank.write(f'Greatest Decrease in Profits : {max_decrease} (${monthly_diff[max_decrease]})\n')

PyBank.close()
