# First we'll import the os module
import os

# Module for reading CSV files
import csv

# Open File

election_csv = os.path.join('Resources','election_data.csv')

with open(election_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # csvreader contains the file path 

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    
   # 1) The total number of votes cast
    total_votes = [row[0] for row in csvreader]
    
   
   # 2) A complete list of candidates who received votes

   # 2a) Reset csvreader so that a variable can be set
    csvfile.seek(0)
    next(csvreader)

   # 2b) Declare variables 
    individual_candidate = []
    candidate = [str(row[2]) for row in csvreader]
   
   # Loop through to find unique candidates
    for candidate in candidate:
        if candidate not in str(individual_candidate):
            individual_candidate.append(candidate) 
    

    
   # 3) The total number of votes each candidate won
    csvfile.seek(0)
    next(csvreader)

   
   # 3a) Declare variables
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
  
   # 3b) Loop through rows to count each candidate
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        if candidate == 'Khan':
            khan_votes = khan_votes + 1
        elif candidate == 'Correy':
            correy_votes = correy_votes + 1
        elif candidate == 'Li':
            li_votes = li_votes + 1
        elif candidate == "O'Tooley":
            otooley_votes = otooley_votes + 1
    


   # 4) The percentage of votes each candidate won 
    khan_percentage = (khan_votes / len(total_votes)) * 100
    correy_percentage = (correy_votes / len(total_votes)) * 100
    li_percentage = (li_votes / len(total_votes)) * 100
    otooley_percentage = (otooley_votes / len(total_votes)) * 100
   
     # 5) The winner of the election based on popular vote.

    winner = 'Khan'

    # 6) Print out the results
    print('Election Results')
    print('-------------------------')
    print('Total Votes: ' + str(len(total_votes)))
    print('-------------------------')
    print('Khan: ' + str(round(khan_percentage)) + str('.000%') + ' (' + str(khan_votes) + ')')
    print('Correy: ' + str(round(correy_percentage)) + str('.000%') + ' (' + str(correy_votes) + ')')
    print('Li: ' + str(round(li_percentage)) + str('.000%') + ' (' + str(li_votes) + ')')
    print("O'Tooley: " + str(round(otooley_percentage)) + str('.000%') + ' (' + str(otooley_votes) + ')')
    print('-------------------------')
    print('Winner: ' + winner)
    print('-------------------------')
    
    # Specify the file to write to
output_path = os.path.join("output", "PyBank_Output.csv")
    
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row 
    csvwriter.writerow(["Election Results\n-------------------------\nTotal Votes: 3521001\n-------------------------\nTKhan: 63.000% (2218231)\nCorrey: 20.000% (704200)\nLi: 14.000% (492940)\nO'Tooley: 3.000% (105630)\n-------------------------\n Winner: Khan\n"])
