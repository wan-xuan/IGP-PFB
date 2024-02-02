from pathlib import Path
import csv

#this function reads the CSV file
def read_csv(file_path):
    with file_path.open(mode='r', encoding='UTF-8', newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        #creates an empty list to store data
        CoH = [] 
        for row in reader:
            #changes the current columns into integer rather than string
            CoH.append((int(row[0]), int(row[1]))) 
        return CoH

#this function analyses the list of tuples representing cash on hand data
def analyse_cash_on_hand(CoH):
    cash_changes = 0
    cash_changesday = 0
    increase = 0
    decrease = 0
    deficits = []

    for i in range(len(CoH) - 1):
    #checks if the previous day's COH is lower than current day's COH, if so that day is an increase 
        if CoH[i][1] < CoH[i+1][1]:
            #increase variable will plus one count everytime the loop's condition is met^
            increase += 1  
            #if after subtracting the current day's COH with the previous is bigger than the previous loop, it will replace the amount stored in the variable, cash_changes
            if (CoH[i+1][1] - CoH[i][1]) > cash_changes: 
                cash_changes = (CoH[i+1][1] - CoH[i][1])
                # Use the day of the second data point (current day)
                cash_changesday = CoH[i+1][0]  

        #checks if the previous day's COH is higher than current day's COH, if so that day is an decrease/deficit 
        else:
            decrease += 1 
            #if after subtracting the previous day's COH with the current's is bigger than the previous loop, it will replace the amount stored in the variable, cash_changes
            if (CoH[i][1] - CoH[i+1][1]) > cash_changes: 
                cash_changes = (CoH[i][1] - CoH[i+1][1])
                # Use the day of the second data point (current day)
                cash_changesday = CoH[i+1][0] 
                print(f"[CASH DEFICIT] DAY: {CoH[i+1][0]}, AMOUNT: SGD{abs(CoH[i][1] - CoH[i+1][1])}") 
             
             #will only print if cash on hand fluctuates (scenario 3)
            elif increase >0 and decrease >0: 
                print(f"[CASH DEFICIT] DAY: {CoH[i+1][0]}, AMOUNT: SGD{abs(CoH[i][1] - CoH[i+1][1])}") 
                #abs was used to remove the (-) sign just like the examples given
                #the code below, adds every deficit calculated and its day to the list 
                deficits.append((abs(CoH[i][1] - CoH[i+1][1]), CoH[i+1][0])) 

    #If always increasing, it will return the output below
    if increase > 0 and decrease == 0:
        return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\
            \n[CASH SURPLUS] DAY:{cash_changesday}, AMOUNT: SGD{cash_changes}"
    #If always decreasing, it will return the output as below
    elif increase == 0 and decrease > 0:
        return f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\
            \n[CASH DEFICIT] DAY:{cash_changesday}, AMOUNT: SGD{cash_changes}"
    else:
        #sorts the data into descending order
        deficits.sort(reverse=True)
    #If COH fluctuates (Scenario 3),  it will return the output below
    return f"[HIGHEST CASH DEFICIT] DAY:{deficits[0][1]}, AMOUNT: SGD{abs(deficits[0][0])}\
        \n[2ND HIGHEST CASH DEFICIT] DAY:{deficits[1][1]}, AMOUNT: SGD{abs(deficits[1][0])}\
        \n[3RD HIGHEST CASH DEFICIT] DAY:{deficits[2][1]}, AMOUNT: SGD{abs(deficits[2][0])}"
