#PyPoll

# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.


#import dependencies
import os
import csv

#open csv and read
csvpath = os.path.join('Resources', 'Homework_03-Python_PyPoll_Resources_election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #initialize
    votes = 0
    candidates = []
    khan = 0
    otooley = 0
    li = 0
    correy = 0

    #loop through rows, grabbing total votes and individual votes to each candidate counter
    for row in csvreader:
        votes += 1
        candidates.append(row[2])
        if row[2] == 'Khan':
            khan += 1
        if row[2] == "O'Tooley":
            otooley += 1
        if row[2] == 'Li':
            li += 1
        if row[2] == 'Correy':
            correy += 1

#stats on vote percentage
unique_cand = set(candidates)
perc_khan = (khan/votes)*100
perc_otooley = (otooley/votes)*100
perc_li = (li/votes)*100
perc_correy = (correy/votes)*100

#create dict with candidate and tallies
compare = {}
compare['Khan'] = khan
compare["O'Tooley"] = otooley
compare['Li'] = li
compare['Correy'] = correy

#find highest value, get its key
winner = max(compare, key=compare.get)

#print to terminal
print('Election Results')
print('------------------------')
print(f"Total Votes: {votes}")
print('------------------------')
#print(f"Candidates: {unique_cand}")
print(f'Khan: {perc_khan:.3f}%  ({khan})')
print(f'Correy: {perc_correy:.3f}%  ({correy})')
print(f'Li: {perc_li:.3f}%  ({li})')
print(f"O'Tooley: {perc_otooley:.3f}%  ({otooley})")
print('------------------------')
print(f'Winner: {winner}')
print('------------------------')

#print to text file
with open('Analysis/PyPoll.txt', 'w') as PyPoll:

    PyPoll.write('Election Results\n')
    PyPoll.write('------------------------\n')
    PyPoll.write(f"Total Votes: {votes}\n")
    PyPoll.write('------------------------\n')  
    PyPoll.write(f'Khan: {perc_khan:.3f}%  ({khan})\n')
    PyPoll.write(f'Correy: {perc_correy:.3f}%  ({correy})\n')
    PyPoll.write(f'Li: {perc_li:.3f}%  ({li})\n')
    PyPoll.write(f"O'Tooley: {perc_otooley:.3f}%  ({otooley})\n")    
    PyPoll.write('------------------------\n')
    PyPoll.write(f'Winner: {winner}\n')
    PyPoll.write('------------------------\n') 

PyPoll.close()