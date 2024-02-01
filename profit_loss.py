from pathlib import Path
import csv

def read_csv(file_path):
    with file_path.open(mode='r', encoding='UTF-8', newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        PnL = []
        for row in reader:
            PnL.append((int(row[0]), int(row[4])))
        return PnL

def analyze_profit_n_loss(PnL):
    profit_n_loss_changes = 0
    profit_n_loss_changesday = 0
    increase = 0
    decrease = 0
    deficits = []

    for i in range(len(PnL) - 1):
        if PnL[i][1] < PnL[i+1][1]:
            increase += 1
            if (PnL[i+1][1] - PnL[i][1]) > profit_n_loss_changes:
                profit_n_loss_changes = (PnL[i+1][1] - PnL[i][1])
                profit_n_loss_changesday = PnL[i+1][0]  # Use the day of the second data point
        else:
            decrease += 1
            print(f"[NET PROFIT DEFICIT] DAY: {PnL[i][0]+1}, AMOUNT: SGD{abs(PnL[i][1] - PnL[i+1][1])}")
            deficits.append((abs(PnL[i][1] - PnL[i+1][1]), PnL[i][0]+1))
            
            if (PnL[i][1] - PnL[i+1][1]) < profit_n_loss_changes:
                profit_n_loss_changes = (PnL[i][1] - PnL[i+1][1])
                profit_n_loss_changesday = PnL[i][0] + 1

    if increase > 0 and decrease == 0:
        return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\
            \n[HIGHEST NET PROFIT SURPLUS] DAY:{profit_n_loss_changesday}, AMOUNT: SGD{profit_n_loss_changes}"
    elif increase == 0 and decrease > 0:
        return f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\
            \n[HIGHEST PROFIT DEFICIT] DAY:{profit_n_loss_changesday}, AMOUNT: SGD{profit_n_loss_changes}"
    else:
        deficits.sort(reverse=True)
        return f"[HIGHEST NET PROFIT DEFICIT] DAY:{deficits[0][1]}, AMOUNT: SGD{abs(deficits[0][0])}\
                \n[2ND  HIGHEST NET PROFIT DEFICIT] DAY:{deficits[1][1]}, AMOUNT: SGD{abs(deficits[1][0])}\
                \n[3RD  HIGHEST NET PROFIT DEFICIT] DAY:{deficits[2][1]}, AMOUNT: SGD{abs(deficits[1][0])}"