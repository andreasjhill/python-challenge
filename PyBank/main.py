# import necessary libraries
import os 
import csv 

# import csv file into Python
file = os.path.join('PyBank/Resources/budget_data.csv')

with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

# total number of months, profit, change in profit included in the dataset
    total_months = []
    profit = []
    change_profit = []

# create the index that will be added
    for row in csvreader:

# adding the first value in the current row to the end of the total_months and profit list.
        total_months.append(row[0])
        profit.append(int(row[1]))

# This loop iterates through each index of the profit list except for the last index (hence the -1), 
# and calculates the difference between the value at the current index and the value at the next index (profit[i+1]-profit[i]). 
# It then appends this difference to the change_profit list.
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])

# define increase and decrease of profit
increase = max(change_profit)
decrease = min(change_profit)

month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

# print results into the terminal 
print("Financial Analysis")
print("-----------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(decrease))})")

# Exporting file to Resources folder 
output = os.path.join('PyBank/Analysis/output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(total_months)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(decrease))})")