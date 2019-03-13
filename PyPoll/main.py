# Modules
import os
import csv
import sys  #needed for writing the txt file

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
# Lists to store data
wVoter = []     #store the worksheet date as a list

# with open(fileName, newline="", encoding='utf-8') as csvfile.   Do I need the 'r'??
with open(csvpath, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader, None)  #skip the header row      
      
    #to determine the number of rows, create a list and count the list
    for row in csvreader:
        
        #print(row)  #use this to confirm I am reading the file
        
        # Add each row to the list fo wVoter
        wVoter.append(row[0])
        
    
    #Leave the For loop, and print results from the two lists
    print("Election Results")
    print("------------------------------------")
    print("Total Months: " + str(len(wVoter)))
    print("------------------------------------")
    
      #Print the data on the screen to a txt file
    #-------------------------------------------
file = open('output.txt', 'w')
file.write("Election Results" + '\n')
file.write("------------------------------------" + '\n')
file.write("Total Months: " + str(len(wVoter)) + '\n')
file.write("------------------------------------" + '\n')
file.close()