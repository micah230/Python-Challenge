import os
import csv

# Find file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Make lists and set counter
columnsum = 0
columns = []
columndate = []

# Fill lists and make basic calculations
with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        columnsum += (int(row[1]))
        columns.append(row[1])
        columndate.append(row[0])
    columncount = (len(columns))
    aveproloss = (columnsum/columncount)

# Calculate changes in values with new list
changelist = [int(columns[i]) - int(columns[i-1]) for i in range(1, len(columns))]
avechange = round(sum(changelist)/int(len(changelist)),2)
highpro = max(changelist)
minpro = min(changelist)

# Find values for corresponding dates
if highpro in changelist:
    highindex = changelist.index(highpro)
if minpro in changelist:
    minindex = changelist.index(minpro)

# Final answers
print("Financial Analysis")
print("----------------------------")
print(f'Total months: {columncount}')
print(f'Total: ${columnsum}')
print(f'Average change: ${avechange}')
print(f'Greatest Increase in Profits: {columndate[highindex+1]} (${highpro})')
print(f'Greatest Decrease in Profits: {columndate[minindex+1]} (${minpro})')

# Set output 
output_file = os.path.join('Analysis', 'Financial Analysis.txt')
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write answers
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f'Total months: {columncount}\n')
    datafile.write(f'Total: ${columnsum}\n')
    datafile.write(f'Average change: ${avechange}\n')
    datafile.write(f'Greatest Increase in Profits: {columndate[highindex+1]} (${highpro})\n')
    datafile.write(f'Greatest Decrease in Profits: {columndate[minindex+1]} (${minpro})\n')


