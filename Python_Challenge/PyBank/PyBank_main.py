# First we'll import the os module
import os

# Module for reading CSV files
import csv

# Open File

budget_csv = os.path.join('Resources','budget_data.csv')

with open(budget_csv, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # csvreader contains the file path 

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

     # 1) The total number of months included in the dataset 
    total_months = [row[0] for row in csvreader]
    print('Total Months: ' + str(len(total_months)))


    # 2) The net total amount of "Profit/Losses" over the entire period
    csvfile.seek(0)
    next(csvreader)

    # 2a) Create a variable to store cloumn 2 as a list
    col2 = [int(row[1]) for row in csvreader]

    # 2b) Calculate the total profit/loss and print the results
    Profit_Loss_total = sum(col2)
    print('Total Profit/Loss: ' + '$' + str(Profit_Loss_total))

    
    # 3) The average of the changes in "Profit/Losses" over the entire period
    previous_value = col2[0]
    profit_loss_diff = 0
    average_change = []
   
    for current_value in col2:
        profit_loss_diff = current_value - previous_value
        average_change.append(profit_loss_diff)
        previous_value = current_value
    Average = sum(average_change[1:])/len(average_change[1:])
    print('Average  Change: ' + str(round(Average, 2)))  



    # 4) The greatest increase in profits (date and amount) over the entire period
    max_value = 0
    date = ""
    t = total_months
    a = average_change
    u = list(zip(t,a))

    for i, k in u:
    
        if k > max_value:
            max_value = k
            date = i
    print('Greatest Increase in Profits: ' + date + ' ' + '(' + '$' + str(max_value) + ')')
   
            

    # 5) The greatest decrease in losses (date and amount) over the entire period
    
    min_value = 9999999
    date = ""
    t = total_months
    a = average_change
    u = list(zip(t,a))

    for i, k in u:
    
        if k < min_value:
            min_value = k
            date = i
    print('Greatest Increase in Profits: ' + date + ' ' + '(' + '$' + str(min_value) + ')')

# Specify the file to write to
output_path = os.path.join("output", "PyBank_Output.csv")
    
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row 
#     csvwriter.writerow(['Financial Analyis\n'])

#     # Write the second row
#     csvwriter.writerow([])
   
#     # Write the third row
#     csvwriter.writerow([])

#     # Write the fourth row
#     csvwriter.writerow([])

#     # Write the fifth row
#     csvwriter.writerow([])

#      # Write the sixth row
#     csvwriter.writerow([])