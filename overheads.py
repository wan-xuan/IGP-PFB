from pathlib import Path
import csv

def read_overheads(file_path):
    with file_path.open(mode='r', encoding='UTF-8', newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        overHead = []
        highest = 0

        for row in reader:
            expense_type = row[0]
            amount = float(row[1])
            overHead.append((expense_type, amount))

        return overHead



