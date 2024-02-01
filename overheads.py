from pathlib import Path
import csv

def read_overheads(file_path):
    with file_path.open(mode='r', encoding='UTF-8', newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        overHead = []
        highest = 0

        for row in reader:
            expense_type = row[0] #type of expenses
            amount = float(row[1]) #percentage of each type out of 100%
            overHead.append((expense_type, amount))

        return overHead

def analyze_highest_overhead(overheads):
    highest_amount = 0
    highest_type = ""

    for expense_type, amount in overheads:
        if amount > highest_amount:
            highest_amount = amount
            highest_type = expense_type

    return f"[HIGHEST OVERHEAD] {highest_type}:{highest_amount}%"

