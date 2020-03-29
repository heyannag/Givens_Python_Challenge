# Objective, create a Python script to run the following:
# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period


#Start by importing the dependencies
import os
import csv

# Defining initial values of variables
months = 0
net_total = 0

# Start by creating a csv variable to easily reference the data
def PyBank(data):
    
    # Collect the total number of months
    months = 0
    # Record the "Profit/Losses" under net total
    net_total = 0
    # Make a list of the weekly profit/losses
    weekly_amount = []
    # Make a list of each week
    weeks = []

    # Begin For loop, for every row in csv:
    for row in data:
        months += 1
        net_total = net_total + int(row[1])
        weekly_amount.append(row[1])
        weeks.append(row[0])

    # Configure a list to show the changes week over week week. This will be used to caluclate the average, min, and max.
    weekly_change = []
    # Begin 'For loop' within the range of weekly_amount
    for i in range(len(weekly_amount)-1):
        weekly_change.append(int(weekly_amount[i+1])-int(weekly_amount[i]))
    
    # Begin 'For loop' to record a list of the weekly_change that will be used to determine min/max
    for j in range(len(weekly_change)-1): 
        if j == 0:
            # State the max and min values
            max_change = weekly_change[0]
            min_change = weekly_change[0]
        else: 
            if weekly_change[j] > max_change:
                max_change = weekly_change[j]
                max_week = weeks[j+1]
            elif weekly_change[j] < min_change:
                min_change = weekly_change[j]
                min_week = weeks[j+1]
            else: #last else statement 
                max_change = max_change
                min_change = min_change

    avg_change  = round(sum(weekly_change)/len(weekly_change),2)

    return [months,net_total,avg_change,max_change,min_change,max_week,min_week]


#Set the path for my csv file
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #Skip the header line
    header = next(csvreader)
    analysis = PyBank(csvreader)

print(f"Total months: {analysis[0]}\nNet Total Profit/Loss: ${analysis[1]}\nAverage Weekly Change: ${analysis[2]}\nMax Weekly Change: {analysis[5]} (${analysis[3]})\nMin Weekly Change: {analysis[6]} (${analysis[4]})")

with open("output_file.txt","w") as text_file:
    text_file.write(f"Total months: {analysis[0]}\nNet Total Profit/Loss: ${analysis[1]}\nAverage Weekly Change: ${analysis[2]}\nMax Weekly Change: {analysis[5]} (${analysis[3]})\nMin Weekly Change: {analysis[6]} (${analysis[4]})")
             
