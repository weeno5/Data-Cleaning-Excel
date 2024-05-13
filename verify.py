# This code verifies whether the data cleaned excel file 
# all contains the centralised keyword that has been set
# in the Codenew.py file and is accounted for
# This is so that no data goes unaccounted for when doing
# calculations and analysis

import pandas as pd # pandas library is for interacting with the excel file
from Codenew import codeRenew

# Read the content of the excel file
pis = pis = pd.read_excel('new.xlsx')

# Function for iterating through each row of a collumn
def verify(code):
    
    # Create an array to match with the data cleaned collumn
    # If the data in a row matches with any of the keyword listed
    # The array will append with a False statement showing it does
    # not need to be accounted 
    # If it wasn't accounted then it will give out a True statement
    # Data not accounted for will need to be changed so that it
    # matches with the words inside the listing or will need to
    # create a new category for uncommon issues
    cat=[]
    
    for i,r in enumerate(code):
        cat.append(True)
        if r in codeRenew: # If the data matches with any of the keyword listed
            cat[i]=False
    return cat

# For 3 collumns
cat1=verify(pis['Code 1'])
cat2=verify(pis['Code 2'])
cat3=verify(pis['Code 3'])

# Appending collumns to the excel file where it shows which data has been accounted for
pis["cat1"]=cat1
pis["cat2"]=cat2
pis["cat3"]=cat3

# Save changes to a new excel file
pis.to_excel("verify.xlsx",index=False)