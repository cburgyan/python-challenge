import csv
import os

csv_filepath = os.path.join(".", "Resources", "budget_data.csv")

results = {"Total Months": 0, "Total": 0, "changesInProfitLosses": [], "Average Changes": 0, "Greatest Increase in Profits": {"monthDay": "", "increaseAmount": 0}, "Greatest Decrease in Profits": {"monthDay": "", "decreaseAmount": 0}}

totalMonths = 0
totalProfLoss = 0
changesInProfLoss = []
averChanges = 0
greatestIncrease = {"monthDay": "", "increaseAmount": 0}
greatestDecrease = {"monthDay": "", "decreaseAmount": 0}


with open(csv_filepath, 'r') as rFile:
    budgetReader = csv.reader(rFile)

    headerRow = next(budgetReader)
    print("hello")
    #numMonths = 0
    prevProfLoss = 0
    firstRowOfData = True
    for row in budgetReader:
        totalMonths += 1
        currentProfLoss = float(row[1])
        totalProfLoss += currentProfLoss
        if firstRowOfData:
            # skip adding a change (currentProfLoss - prevProfLoss) to profit/loss since there is no PREVIOUS profit/loss before the first row
            firstRowOfData = False
        else:
            # add a change (currentProfLoss - prevProfLoss) to profit/loss
            changesInProfLoss.append(currentProfLoss - prevProfLoss)
        prevProfLoss = currentProfLoss
        
        if len(changesInProfLoss) > 0:
            if changesInProfLoss[-1] > greatestIncrease["increaseAmount"]:
                greatestIncrease['monthDay'] = row[0]
                greatestIncrease["increaseAmount"] = changesInProfLoss[-1]
            elif changesInProfLoss[-1] < greatestDecrease["decreaseAmount"]:
                greatestDecrease['monthDay'] = row[0]
                greatestDecrease["decreaseAmount"] = changesInProfLoss[-1]

averChanges = sum(changesInProfLoss) / len(changesInProfLoss)

print(f"Total Months: {totalMonths}")
print(f"Total: ${int(totalProfLoss)}")
print(f"Average Change: ${averChanges:.2f}")
print(f"Greatest Increase in Profiles: {greatestIncrease['monthDay']} (${int(greatestIncrease['increaseAmount'])})")
print(f"Greatest Decrease in Profiles: {greatestDecrease['monthDay']} (${int(greatestDecrease['decreaseAmount'])})")

        
        
    #print(numMonths)

