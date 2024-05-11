import pandas as pd
from codenew import codeRenew

pis = pis = pd.read_excel('newreal.xlsx')

def verify(code):
    cat=[]
    for i,r in enumerate(code):
        cat.append(True)
        if r in codeRenew:
            cat[i]=False
    return cat

cat1=verify(pis['Code 1'])
cat2=verify(pis['Code 2'])
cat3=verify(pis['Code 3'])

pis["cat1"]=cat1
pis["cat2"]=cat2
pis["cat3"]=cat3

print(cat1)

pis.to_excel("verify.xlsx",index=False)