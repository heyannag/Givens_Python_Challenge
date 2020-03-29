# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Create path to open CSV file
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    data = []

    # Read each row of data after the header
    for row in csvreader:
        data.append(row)
       
def vote_count(data):
    candidates = {}
    total_votes = 0 
    for row in data[0:10]:
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    return(vote_count)
        
def vote_perecents(candidates, total_votes):
    percents = {}
    for candidate, votes in candidates.items():
        percents[candidate] = (votes/total_votes) * 100
    return percents

def print_results(candidates, percents):
    winning_votes = 0
    winner = ""
    for candidate, votes in candidate.items():
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes

# vote_csv = csvpath('Resources', 'election_data.csv')
# candidates, total_votes = vote_count(vote_csv)
# percents = vote_perecents(candidates, total_votes)
# print(percents)