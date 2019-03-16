#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Modules
import os
import csv
import sys  #needed for writing the txt file
import datetime #needed to convert the date of birth


# In[2]:


# Set path for file
csvpath = os.path.join("Resources", "employee_data.csv")

l_orig_ID = []  #original ID column from the worksheet
l_orig_name = []   #original name from the worksheet
l_orig_dob = []  #original date of birth from the worksheet
l_orig_ssn = []  #original social security number from the worksheet
l_orig_state = []  # original state from the worksheet

with open(csvpath, newline="", encoding='utf-8') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader, None)  #skip the header row  
    
    for row in csvreader:
        #print(row)  #use this to confirm I am reading the file
        
        # Create a list for each row.
        l_orig_ID.append(row[0])
        l_orig_name.append(row[1])
        l_orig_dob.append(row[2])
        l_orig_ssn.append(row[3])
        l_orig_state.append(row[4])  
        

#let the user know what is happening.
print("This script will format the employee list.  Please wait while the file is formatted.")


# In[3]:


#Create a list of first and last names

l_formatted_lastName = []
l_formatted_firstName = []

for each in l_orig_name:
    l_formatted_firstName.append(each.split()[0])
    l_formatted_lastName.append(each.split()[1])
    #each = each.split()[1]
    #l_formatted_lastName.append(each)  #Create a new list of formatted last names

#Tried this ine one for loop, but it always returned the last name.   This can be more efficient.
    
#for each in l_orig_name:
    #each = each.split()[0]
    #l_formatted_firstName.append(each)  #Create a new list of formatted first names
    
     #check the list
#l_formatted_lastName[0:10] , l_formatted_firstName[0:10]   #check the list


# In[4]:


#Create a list of formatted DOB
l_formatted_dob = []

for each in l_orig_dob:
    each = datetime.datetime.strptime(str(each), "%Y-%m-%d").strftime("%m/%d/%Y")
    l_formatted_dob.append(each)
    
#l_formatted_dob[1:10]


# In[5]:


#Create a list of formatted social security numbers

l_formatted_ssn = []  #define the new social security list

for each in l_orig_ssn:
    each = ("***-**-" + each[7] + each[8] + each[9] + each[10])  #create the mask, then populate with the index values
    l_formatted_ssn.append(each)  #Create a new list of formatted social security numbers
    
#l_formatted_ssn[1:10]


# In[6]:


#Add the state library
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[7]:


#Replace the state abbreviations

l_formatted_state = []  #define the new state list

def replace(listName, dictionaryName):

    for i in listName:
        if i in dictionaryName:
            l_formatted_state.append(dictionaryName[i])
        else:
          l_formatted_state.append(i)

replace(l_orig_state, us_state_abbrev)
        
#l_formatted_state[0:10]


# In[8]:


# Zip lists together
cleaned_csv = zip(l_formatted_lastName, l_formatted_firstName, l_formatted_dob, l_formatted_ssn, l_formatted_state)

# Set variable for output file
output_file = os.path.join("employeeData_formatted.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["LastName", "FirstName", "DateOfBirth", "SocialSecurityNumber",
                     "State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)


# In[ ]:

#-------------------------------------------------------
#Let the user know the process is complete and where they can find the file.
print("")
print("")
print("The script is complete!")
print("The formatted file is called employeeData_formatted.csv and located in the same directory as this script.")

