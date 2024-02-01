from pathlib import Path
import csv

def read_csv(file_path):
    with file_path.open(mode='r', encoding='UTF-8', newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        CoH = []
        for row in reader:
            CoH.append((int(row[0]), int(row[1])))
        return CoH

def analyze_cash_on_hand(CoH):
    cash_changes = 0
    cash_changesday = 0
    increase = 0
    decrease = 0
    deficits = []

    for i in range(len(CoH) - 1):
        if CoH[i][1] < CoH[i+1][1]:
            increase += 1
            if (CoH[i+1][1] - CoH[i][1]) > cash_changes:
                cash_changes = (CoH[i+1][1] - CoH[i][1])
                cash_changesday = CoH[i+1][0]  # Use the day of the second data point
        else:
            decrease += 1
            print(f"[CASH DEFICIT] DAY: {CoH[i][0]+1}, AMOUNT: SGD{abs(CoH[i][1] - CoH[i+1][1])}")
            deficits.append((abs(CoH[i][1] - CoH[i+1][1]), CoH[i][0]+1))
            
            if (CoH[i][1] - CoH[i+1][1]) < cash_changes:
                cash_changes = (CoH[i][1] - CoH[i+1][1])
                cash_changesday = CoH[i][0] + 1

    if increase > 0 and decrease == 0:
        return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\
            \n[CASH SURPLUS] DAY:{cash_changesday}, AMOUNT: SGD{cash_changes}"
    elif increase == 0 and decrease > 0:
        return f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\
            \n[CASH DEFICIT] DAY:{cash_changesday}, AMOUNT: SGD{cash_changes}"
        

    else:

        deficits.sort(reverse=True)

        return f"[HIGHEST CASH DEFICIT] DAY:{deficits[0][1]}, AMOUNT: SGD{abs(deficits[0][0])}\
        \n[2ND HIGHEST CASH DEFICIT] DAY:{deficits[1][1]}, AMOUNT: SGD{abs(deficits[1][0])}\
        \n[3RD HIGHEST CASH DEFICIT] DAY:{deficits[2][1]}, AMOUNT: SGD{abs(deficits[2][0])}"