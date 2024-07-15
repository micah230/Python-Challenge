import os
import csv

# Find file
csvpath = os.path.join('Resources', 'election_data.csv')

# Make lists 
candlist = []
voterid = []
candidate = []

# Fill lists
with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        candidate.append(row[2])
        voterid.append(row[0])
        
        for i in range(2, len(row)):
            if row[i] not in candlist:
                candlist.append(row[i])

# Basic calculations and more lists 
totalvotes = len(voterid)
cand1 = []
cand2 = []
cand3 = []
    
# Sort votes by candidate
for candidates in candidate: 
    if candidates == candlist[0]:
        cand1.append(candidates)
    elif candidates == candlist[1]:
        cand2.append(candidates) 
    elif candidates == candlist[2]:
        cand3.append(candidates)

# Create new list of final percentages and determine winner
finals = [round(((len(cand1))/totalvotes)*100,3), round(((len(cand2))/totalvotes)*100,3), round(((len(cand3))/totalvotes)*100,3)]
winner = finals.index(max(finals))

# Final answers
print("Election Results")
print("-------------------------")
print(f'Total Votes: {totalvotes}')
print("-------------------------")
print(f'{candlist[0]}: {finals[0]}% ({len(cand1)})')
print(f'{candlist[1]}: {finals[1]}% ({len(cand2)})')
print(f'{candlist[2]}: {finals[2]}% ({len(cand3)})')
print("-------------------------")
print(f'Winner: {candlist[(winner)]}')
print("-------------------------")

# Set output 
output_file = os.path.join('Analysis', 'Election Results.txt')
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write answers
    datafile.write("Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write(f'Total Votes: {totalvotes}\n')
    datafile.write("-------------------------\n")
    datafile.write(f'{candlist[0]}: {finals[0]}% ({len(cand1)})\n')
    datafile.write(f'{candlist[1]}: {finals[1]}% ({len(cand2)})\n')
    datafile.write(f'{candlist[2]}: {finals[2]}% ({len(cand3)})\n')
    datafile.write("-------------------------\n")
    datafile.write(f'Winner: {candlist[(winner)]}\n')
    datafile.write("-------------------------\n")