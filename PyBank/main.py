import csv
import os

monthsList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# makeExceptions is a control variable to ask user if there should be an exception for an, otherwise, invalid month designation
makeExceptions = True

def AddOnlyAValidMonth(row):
    global makeExceptions

    # Check to make sure row has valid data
    if len(row) != 0:
        if row[0][:3] in monthsList:
            # This is a valid month designation return 1 valid month
            return 1
        else:
            if makeExceptions:
                # perhaps a month is just mispelled (eg "Jna" instead of "Jan")
                rowIsValid = input(f'Does this, "{row[0][:3]}" have a valid month? (y)es or (n)o or no-and-(m)ake-no-more-exceptions')
                if rowIsValid == 'y':
                    monthsList.add(row[0][:3])

                    # This is a valid month designation return 1 valid month
                    return 1
                elif rowIsValid == 'm':
                    makeExceptions = False
                    
    # Not a valid month designation so return 0
    return 0



csv_filepath = os.path.join(".", "Resources", "budget_data.csv")



with open(csv_filepath, 'r') as rFile:
    budgetReader = csv.reader(rFile)

    headerRow = next(budgetReader)
    print("hello")
    numMonths = 0
    for row in budgetReader:
        numMonths += AddOnlyAValidMonth(row)
        
        

        
        
    print(numMonths)

