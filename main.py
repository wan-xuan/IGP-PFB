from pathlib import Path
import coh
import profit_loss
import overheads

# Defines file path
fp = Path.cwd() / "Cash_on_Hand.csv"
np = Path.cwd() / "Profit_and_Loss.csv" 
qp = Path.cwd() / "Overheads.csv" 

#imports data to its variable
cash_on_hand_data = coh.read_csv(fp)
profit_loss_data = profit_loss.read_csv(np)
overheads_data = overheads.read_overheads(qp)

# uses the function imported from the modules
if overheads_data:
    highest_overhead_result = overheads.analyse_highest_overhead(overheads_data)
    print(highest_overhead_result)  
else: #lets you know if dataset provided is invalid
    print("No data found in the Overheads file") 

# uses the function imported from the modules
if cash_on_hand_data:
    cash_on_hand_result = coh.analyse_cash_on_hand(cash_on_hand_data)
    print(cash_on_hand_result)
else: #lets you know if dataset provided is invalid
    print("No data found in the Cash-On-Hand file")

# uses the function imported from the modules
if profit_loss_data:
    profit_loss_result = profit_loss.analyse_profit_n_loss(profit_loss_data) 
    print(profit_loss_result)
else: #lets you know if dataset provided is invalid
    print("No data found in the Profit and Loss file") 
# ends at the last module imported----Profit and Loss


