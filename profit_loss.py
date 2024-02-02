from pathlib import Path
import csv

#this function reads the CSV file
def read_csv(file_path):
    with file_path.open(mode='r', encoding='UTF-8', newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        #creates an empty list to store data
        PnL = []
        for row in reader:
            #changes the current columns into integer rather than string
            PnL.append((int(row[0]), int(row[4])))
        return PnL

 #this function analyses the list of tuples representing profit and loss data
def analyse_profit_n_loss(PnL):
    profit_n_loss_changes = 0
    profit_n_loss_changesday = 0
    increase = 0
    decrease = 0
    deficits = []

    for i in range(len(PnL) - 1):
        #checks if the previous day's PNL is lower than current day's PNL, if so that day is an increase
        if PnL[i][1] < PnL[i+1][1]:
             #increase variable will plus one count everytime the loop's condition is met^
            increase += 1
            #if after subtracting the current day's PNL with the previous is bigger than the previous loop, it will replace the amount stored in the variable, profit_n_loss_changes
            if (PnL[i+1][1] - PnL[i][1]) > profit_n_loss_changes:
                profit_n_loss_changes = (PnL[i+1][1] - PnL[i][1])
                # Use the day of the second data point (current day)
                profit_n_loss_changesday = PnL[i+1][0]  

        #checks if the previous day's PNL is higher than current day's PNL, if so that day is an decrease/deficit 
        else: 
            decrease += 1 
            if (PnL[i][1] - PnL[i+1][1]) > profit_n_loss_changes: 
                profit_n_loss_changes = (PnL[i][1] - PnL[i+1][1])
                # Use the day of the second data point (current day) 
                profit_n_loss_changesday = PnL[i+1][0]
                print(f"[NET PROFIT DEFICIT] DAY: {PnL[i+1][0]}, AMOUNT: SGD{abs(PnL[i][1] - PnL[i+1][1])}") 
             
            #will only print if profit and loss fluctuates (scenario 3)
            elif increase >0 and decrease >0: 
                print(f"[NET PROFIT DEFICIT] DAY: {PnL[i+1][0]}, AMOUNT: SGD{abs(PnL[i][1] - PnL[i+1][1])}")
                #abs was used to remove the (-) sign just like the examples given
                #the code below, adds every deficit calculated and its day to the list 
                deficits.append((abs(PnL[i][1] - PnL[i+1][1]), PnL[i+1][0])) 

    #If always increasing, it will return the output below            
    if increase > 0 and decrease == 0:
        return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\
            \n[HIGHEST NET PROFIT SURPLUS] DAY:{profit_n_loss_changesday}, AMOUNT: SGD{profit_n_loss_changes}"
    #If always decreasing, it will return the output below
    elif increase == 0 and decrease > 0:
        return f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\
            \n[HIGHEST PROFIT DEFICIT] DAY:{profit_n_loss_changesday}, AMOUNT: SGD{profit_n_loss_changes}"
    else:
        #sorts the data into descending order
        deficits.sort(reverse=True)
    #If PNL fluctuates (Scenario 3),  it will return the output below    
    return f"[HIGHEST NET PROFIT DEFICIT] DAY:{deficits[0][1]}, AMOUNT: SGD{abs(deficits[0][0])}\
        \n[2ND  HIGHEST NET PROFIT DEFICIT] DAY:{deficits[1][1]}, AMOUNT: SGD{abs(deficits[1][0])}\
        \n[3RD  HIGHEST NET PROFIT DEFICIT] DAY:{deficits[2][1]}, AMOUNT: SGD{abs(deficits[2][0])}"