from pathlib import Path
import csv

#this function reads the CSV file
def read_overheads(file_path):
    with file_path.open(mode='r', encoding='UTF-8', newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        #creates an empty list to store data
        overHead = []

        for row in reader:
            #type of expenses
            expense_type = row[0]
            #percentage of each type out of 100%, as a decimal
            amount = float(row[1])
            #allocate the names(variable) to the rows 
            overHead.append((expense_type, amount))

        return overHead

#this function analyses the list of tuples representing the overhead data
def analyse_highest_overhead(overheads):
    #variable starting at 0, coded to store the highest number comparing to that of the previous loop
    highest_amount = 0
    # str to be filled in by expense_type
    highest_type = ""

    for expense_type, amount in overheads:
        if amount > highest_amount:
            highest_amount = amount
            highest_type = expense_type

    #returns the output for all kind of scenarios
    return f"[HIGHEST OVERHEAD] {highest_type}:{highest_amount}%"