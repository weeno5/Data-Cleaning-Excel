# This code is for cleaning data in an excel file for a research project on student's mental health
# The Excel file is private

# The excel file had inconsistent data with varying strings that describes the same word
# For example, the data that describes the issue with a student may be "ANXIOUS",
# whereas in another row, another student has the issue "anxiety"
# These two different words describe the same issue but the computer does not understand that
# To make meaningful calculations and analysis, we must clean the data first

import pandas as pd # pandas library is for interacting with the excel file
from Codenew import codeRenew

# Read the content of the excel file
pis = pd.read_excel('cisdata.xlsx', sheet_name='Presenting Issues Coding')

# Keywords to be looking out for to funnel them into one centralised word
keywordList=[
         ["FAMILY"],#1
         ["ANGER","ANGRY"],#2
         ["PEER","BULLY"],#3
         ["SEXUAL ABUSE"],#4
         ["SUICID"],#5
         ["HARM"],#6
         ["ESTEEM"],#7
         ["PHYSICAL"],#8
         ["UNWILLING"],#9
         ["SLEEP"],#10
         ["GRIEF"],#11
         ["ANXIETY","ANXIOUS"],#12
         ["STRESS"],#13
         ["TEACHER"],#14
         ["GENERAL","DEPRESS","SAD"],#15
         ["SHY"],#16
         ["IDENTITY"],#17
         ["FIGHT"],#18
         ["NEW BABY"],#19
         ["WITNESS ABUSE"],#20
         ["OVERPROTECTION"],#21
         ["TRAUNCY","TRUANCY"],#22
         ["CHECK"]#23
         ]

# Function for data cleaning a collumn
def clean(code):
    
    # Create an array to match with the data cleaned collumn
    # If the data in a row has been changed/cleaned
    # The array will append with a True statement showing
    # it has been cleaned/changed
    # If it was not changed then it will give out a False statement
    # Unchanged data indicates theres data that has not been cleaned
    change=[] 
    
    # Iterate through all rows
    for i in range(len(code)):
        change.append(False)
        for j,keywordSubList in enumerate(keywordList): # Iterate through the keywords to see if theres any match
            for keyword in keywordSubList:
                if keyword in (str(code[i])).upper():
                    code[i]=codeRenew[j]
                    change[len(change)-1]=True # Change has been made
                    break
    return change

# Students may have multiple issues so there are multiple collumns for additional issues
# Meaning more data to clean
clean1=clean(pis['Code 1'])
clean2=clean(pis['Code 2'])
clean3=clean(pis['Code 3'])

# Appending collumns to the excel file where it shows which data has been changed
pis['clean1']=clean1
pis['clean2']=clean2
pis['clean3']=clean3

# Create a new excel file with the changes
pis.to_excel('New.xlsx',index=False)