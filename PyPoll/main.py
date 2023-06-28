import csv
import os

# Create Path to Data
csv_filepath = os.path.join(".", "Resources", "election_data.csv")

# Initialize variables
totalNumVotes = 0
candidatesDict = {}

#Extract and Tabulate Data
with open(csv_filepath, 'r') as rFile:
    electionReader = csv.reader(rFile)

    # Skip header row
    headerRow = next(electionReader)

    for row in electionReader:
        totalNumVotes += 1

        if row[2] not in candidatesDict:
            candidatesDict[row[2]] = 1
        else:
            candidatesDict[row[2]] += 1

winnerName = ""
winnerVotes = 0

# Create path for results.txt file
resultsFile = os.path.join(".", "analysis", "results.txt")

# Export Financial Analysis results to results.txt file
with open(resultsFile, 'w') as outFile:
    writer = csv.writer(outFile)

    # Print Screen and results.txt file the division line and heading
    print('Election Results\n-------------------------') 
    writer.writerow(['Election Results'])
    writer.writerow(['-------------------------'])
    
    # Print Screen and results.txt file the Total Votes
    print(f'Total Votes: {totalNumVotes}')  
    writer.writerow([f'Total Votes: {totalNumVotes}']) 
    
    # Print Screen and results.txt file the division line
    print('-------------------------')    
    writer.writerow(['-------------------------'])

    isFirstCandidate = True 
    for candidate,votes in candidatesDict.items():

        # Test if current candidate is the winner
        if votes > winnerVotes:
            winnerName = candidate
            winnerVotes = votes
        
        # Print Screen and results.txt file the candidate and his/her percentage of votes and number of votes
        print(f'{candidate}: {votes / totalNumVotes * 100:.3f}% ({votes})')
        writer.writerow([f'{candidate}: {votes / totalNumVotes * 100:.3f}% ({votes})'])

    # Print Screen and results.txt file the division line
    print('-------------------------')
    writer.writerow(['-------------------------'])
    
    # Print Screen and results.txt file the winner's name
    print(f'Winner: {winnerName}')
    writer.writerow([f'Winner: {winnerName}'])
    
    # Print Screen and results.txt file the division line
    print('-------------------------')
    writer.writerow(['-------------------------'])
