# Modules
import os
import csv
import sys  #needed for writing the txt file

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Lists to store data
wCandidate = []   #store the worksheet Candidate column as a list
candidateList = []  #List of candidate names 
candidateTotal = []  #List of candidate totals  

with open(csvpath, newline="", encoding='utf-8') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader, None)  #skip the header row      
      
    #to determine the number of rows, create a list and count the list
    for row in csvreader:
        
        #print(row)  #use this to confirm I am reading the file
        
        # Add each row to the list for wCandidate
        wCandidate.append(row[2])     
    
    #Leave the For loop, and print results from the two lists to the screen and to the file.
    
    print("Election Results")
    print("------------------------------------")
    print("Total Votes: " + str(len(wCandidate)))
    print("------------------------------------")
    
    #write to the output file
    file = open('output.txt', 'w')   # this seems inefficient to leave this open throughout the processing.   Needed because my print results for each candidate are in a for loop.
    
    file.write("Election Results" + '\n')
    file.write("------------------------------------" + '\n')
    file.write("Total Votes: " + str(len(wCandidate)) + '\n')
    file.write("------------------------------------" + '\n')
   

    #Calculate FOR EACH CANDIDATE, the total votes received and the percentage votes received
    for each in candidateList:
        cCount = wCandidate.count(each)  # count the number of times each candidate is listed
        cPercent = round(((cCount / len(wCandidate))*100),5)  #calcualte percentage of total votes for each candidate ??rounds to one digit due to total.   Ask a TA
    
        print(each + ":   "  + str(cPercent) +  "%    (" + str(cCount) + ")")
        file.write(each + ":   "  + str(cPercent) +  "%    (" + str(cCount) + ")" + '\n')
    
        candidateList.append(each)  #Create a new list of only candidate names.  
        candidateTotal.append(cCount) #Create a new list of only candidate totals.
    
     #Leave the for loop
    
    print("------------------------------------")
    file.write("------------------------------------" + '\n')
    
    #Use max to find the winner
    
    winner = candidateTotal.index(max(candidateTotal))  #returns the index number of the highest number of votes
    print("Winner:  " +  str(candidateList[(winner)]) )  #based on the index number, print the winner's name
    print("------------------------------------")
    
    file.write("Winner:  " +  str(candidateList[(winner)]) + '\n' )  
    file.write("------------------------------------" + '\n')
    
file.close()