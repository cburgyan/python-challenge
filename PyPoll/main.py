import csv
import os

# Create Path to Data
csv_filepath = os.path.join(".", "Resources", "election_data.csv")

# Initialize variables of total number of votes and a dictionary for the 
# candidates (keys) and their respective votes (values) they got
totalNumVotes = 0
candidatesDict = {}

#Extract and Tabulate Data
with open(csv_filepath, 'r') as rFile:
    electionReader = csv.reader(rFile)

    # Skip header row
    headerRow = next(electionReader)

    # Tabulate candidate's votes
    for row in electionReader:
        totalNumVotes += 1

        # Check if row[2] is a new candidate and if so, add the candidate to the 
        # candidate dictionary along with a vote count of 1
        if row[2] not in candidatesDict:
            candidatesDict[row[2]] = 1
        else:
            candidatesDict[row[2]] += 1

# Initialize winner variables
winnerName = ""
winnerVotes = 0

# Create path for results.txt file
resultsFile = os.path.join(".", "analysis", "results.txt")

# Export Election results to results.txt file and print results to screen
with open(resultsFile, 'w') as outFile:
    writer = csv.writer(outFile)

    # Print to Screen and results.txt file the results
    print('\nElection Results\n')
    writer.writerow(['Election Results'])
    print('-------------------------\n') 
    writer.writerow(['-------------------------'])
    print(f'Total Votes: {totalNumVotes}\n')  
    writer.writerow([f'Total Votes: {totalNumVotes}']) 
    print('-------------------------\n')    
    writer.writerow(['-------------------------'])

    # Print each candidate, his/her percentage, his/her total, and determine if he/she is the winner
    for candidate,votes in candidatesDict.items():

        # Test if current candidate is the winner
        if votes > winnerVotes:
            winnerName = candidate
            winnerVotes = votes
        
        # Print Screen and results.txt file the candidate and his/her percentage of votes and number of votes
        print(f'{candidate}: {votes / totalNumVotes * 100:.3f}% ({votes})\n')
        writer.writerow([f'{candidate}: {votes / totalNumVotes * 100:.3f}% ({votes})'])

    # Print Screen and results.txt file the winner results
    print('-------------------------\n')
    writer.writerow(['-------------------------'])
    print(f'Winner: {winnerName}\n')
    writer.writerow([f'Winner: {winnerName}'])
    print('-------------------------\n')
    writer.writerow(['-------------------------'])
