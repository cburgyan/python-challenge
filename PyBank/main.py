import csv
import os

# Create Path to Data
csv_filepath = os.path.join(".", "Resources", "budget_data.csv")

# Initialize variables
totalMonths = 0
totalProfLoss = 0
changesInProfLoss = []
averChanges = 0
greatestIncrease = {"monthDay": "", "increaseAmount": 0}
greatestDecrease = {"monthDay": "", "decreaseAmount": 0}

#Extract and Tabulate Data
with open(csv_filepath, 'r') as rFile:
    budgetReader = csv.reader(rFile)

    # Skip header row
    headerRow = next(budgetReader)

    # Initialize Variables
    prevProfLoss = 0
    isfirstRowOfData = True

    # Iterate through rows from file
    for row in budgetReader:
        totalMonths += 1
        currentProfLoss = float(row[1])
        totalProfLoss += currentProfLoss

        # When collecting the changesInProfLoss, the first row must be skipped because when the FIRST row is the CURRENT row, then there is NO PREVIOUS row by definition
        if isfirstRowOfData:
            # skip adding a change (currentProfLoss - prevProfLoss) to profit/loss since there is no PREVIOUS profit/loss before the first row
            isfirstRowOfData = False
        else:
            # add a change (currentProfLoss - prevProfLoss) to profit/loss
            changesInProfLoss.append(currentProfLoss - prevProfLoss)

        # Set new previous row of profit/losses from current row
        prevProfLoss = currentProfLoss
        
        # Make sure changesInProfLoss is not an empty list
        if len(changesInProfLoss) > 0:

            # Check if a new Greatest Increase or new Greatest Decrease has been ben found
            if changesInProfLoss[-1] > greatestIncrease["increaseAmount"]:
                # Record the new greatest increase amount and date
                greatestIncrease['monthDay'] = row[0]
                greatestIncrease["increaseAmount"] = changesInProfLoss[-1]
            elif changesInProfLoss[-1] < greatestDecrease["decreaseAmount"]:
                # Record the new greatest decrease amount and date
                greatestDecrease['monthDay'] = row[0]
                greatestDecrease["decreaseAmount"] = changesInProfLoss[-1]

# Calculate Average Change in Profit/Losses
averChanges = sum(changesInProfLoss) / len(changesInProfLoss)

# Create path for results.txt file
resultsFile = os.path.join(".", "analysis", "results.txt")

# Export Financial Analysis results to results.txt file and print the results to screen
with open(resultsFile, 'w') as outFile:
    writer = csv.writer(outFile)

    # Print to screen and results.txt the results
    writer.writerow(["Financial Analysis"])
    print("\nFinancial Analysis\n")

    writer.writerow(["----------------------------"])
    print("----------------------------\n")

    writer.writerow([f"Total Months: {totalMonths}"])
    print(f"Total Months: {totalMonths}\n")

    writer.writerow([f"Total: ${int(totalProfLoss)}"])
    print(f"Total: ${int(totalProfLoss)}\n")

    writer.writerow([f"Average Change: ${averChanges:.2f}"])
    print(f"Average Change: ${averChanges:.2f}\n")

    writer.writerow([f"Greatest Increase in Profits: {greatestIncrease['monthDay']} (${int(greatestIncrease['increaseAmount'])})"])
    print(f"Greatest Increase in Profits: {greatestIncrease['monthDay']} (${int(greatestIncrease['increaseAmount'])})\n")
    
    writer.writerow([f"Greatest Decrease in Profits: {greatestDecrease['monthDay']} (${int(greatestDecrease['decreaseAmount'])})"])
    print(f"Greatest Decrease in Profits: {greatestDecrease['monthDay']} (${int(greatestDecrease['decreaseAmount'])})\n")

