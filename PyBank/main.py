import csv
import os

def GetTotalNumberOfMonths(budgetReader):
    setOfMonths = set()
    for row in budgetReader:
        setOfMonths.add(row[0][:3])
    print(setOfMonths)
    return len(setOfMonths)



csv_filepath = os.path.join(".", "Resources", "budget_data.csv")

monthsList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


with open(csv_filepath, 'r') as rFile:
    budgetReader = csv.reader(rFile)

    headerRow = next(budgetReader)
    print("hello")
    numMonths = 0
    for row in budgetReader:

        # Check to make sure row has valid data
        if len(row) != 0:
            if row[0][:3] in monthsList:
                numMonths += 1
            else:
                # perhaps a month is just mispelled (eg "Jna" instead of "Jan")
                rowIsValid = input(f'Does this, "{row[0]}" have a valid month? (y)es or (n)o ')
                if rowIsValid == 'y':
                    numMonths += 1
        

        
        
    print(numMonths)

