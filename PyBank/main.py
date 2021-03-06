# Modules
import os
import csv
import sys  #needed for writing the txt file

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
wDate = []     #store the worksheet date as a list
wProfit = []   #store the worksheet profit loss column as a list
wRunAvg = []   #store the running averages for profit Loss column

# with open(fileName, newline="", encoding='utf-8') as csvfile.   Do I need the 'r'??
with open(csvpath, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader, None)  #skip the header row      
      
    #to determine the number of rows, create a list and count the list
    for row in csvreader:
        
        #print(row)  #use this to confirm I am reading the file
        
        # Add the list for worksheet Date
        wDate.append(row[0])
        
        #Add the list for worksheet profit and loss
        wProfit.append(row[1])
    
    #--------Create a new list, which shows the change in each month
    #---------begin by creating  function which will perform the calculation to find the change in each month
    
    def fRunAvg(peaches):
        for i in range(len(peaches)):
            wRunAvg.append(peaches[i]-peaches[i-1])
        #print("All done.   Print runAvg to see the averages.") #included to check my work.
    
    #-------Pass this function the profit/loss list as a FLOAT.
    
    fRunAvg([float(n) for n in wProfit])  
    wRunAvg.pop(0) #pop out the first number re:  there is no change the first month of the list
    #print(wRunAvg)  #Confirm the values.  CONGRATULATIONS!  you now have a list of the changes from month to month.

    #-----add function to average the changes
    
    #create a function to average a list of numbers
    def fAverage(numbers):
        length = len(numbers)
        total = 0.0
        for each in numbers:
            total += each
        return total / length
    
    averageChange = round(fAverage(wRunAvg),2)  #  Call the function to average the list called wRunAvg
    
    #----------Determine the Maximum and Minimum Change - #Problem - Try to use a function.
    maxIndex = wRunAvg.index(max(wRunAvg))
    minIndex = wRunAvg.index(min(wRunAvg))
    
    #------zip the three lists

    cleaned_csv = zip(wDate, wProfit, wRunAvg)

    # Set variable for output file
    output_file = os.path.join("web_final_PyBank.csv")

    #  Open the output file
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)

        # Write the header row
        writer.writerow(["Date", "Profit/Losses", "P/L Change"])

        # Write in zipped rows
        writer.writerows(cleaned_csv)
            
    #Print Results
    print("Financial Analysis")
    print("------------------------------------")
    print("Total Months: " + str(len(wDate))) 
    print("The Total Profit/Loss: " + str(sum(map(float, wProfit))))   #could also have used an int instead of float for this data set.
    print("Average Change: " + str(averageChange)) 
    print("Greatest Increase in Profits: " + (wDate[(maxIndex)]) + "- (" + str(wRunAvg[(maxIndex)]) +")")
    print("Greatest Decrease in Profits: " + (wDate[(minIndex)]) + "- (" + str(wRunAvg[(minIndex)]) +")")



    #Print the data on the screen to a txt file
    #-------------------------------------------
file = open('output.txt', 'w')
file.write("Financial Analysis" + '\n')
file.write("------------------------------------" + '\n')
file.write("Total Months: " + str(len(wDate)) + '\n')
file.write("The Total Profit/Loss: " + str(sum(map(float, wProfit))) + '\n')   #could also have used an int instead of float for this data set.
file.write("Average Change: " + str(averageChange) + '\n')
file.write("Greatest Increase in Profits: " + (wDate[(maxIndex)]) + "- (" + str(wRunAvg[(maxIndex)]) +")" +'\n')
file.write("Greatest Decrease in Profits: " + (wDate[(minIndex)]) + "- (" + str(wRunAvg[(minIndex)]) +")" +'\n')
file.close()