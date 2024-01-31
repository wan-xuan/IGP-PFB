from pathlib import Path
import coh
import profit_loss
import overheads

# Define file paths
fp = Path.cwd() / "surplus.csv" #cash-on-hand-sgd.csv
np = Path.cwd() / "deficit.csv" #profit-and-loss-sgd.csv
qp = Path.cwd() / "overheads-day-90.csv" #overheads-day-90.csv

# Use functions from the imported modules
cash_on_hand_data = coh.read_csv(fp)
profit_loss_data = profit_loss.read_csv(np)
overheads_data = overheads.read_overheads(qp)

if overheads_data:
    highest_overhead_result = overheads.analyze_highest_overhead(overheads_data)
    print(highest_overhead_result)
else:
    print("No data found in the Overheads file")



