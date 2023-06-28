import csv
import os

monthsList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def AddOnlyAValidMonth(row):
    # Check to make sure row has valid data
    if len(row) != 0:
        if row[0][:3] in monthsList:
            return 1
        else:
            # perhaps a month is just mispelled (eg "Jna" instead of "Jan")
            rowIsValid = input(f'Does this, "{row[0]}" have a valid month? (y)es or (n)o ')
            if rowIsValid == 'y':
                return 1
            
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

