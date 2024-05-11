import pandas as pd
from codenew import codeRenew

pis = pd.read_excel('cisdata.xlsx', sheet_name='Presenting Issues Coding')

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

def clean(code):
    change=[]
    for i in range(len(code)):
        change.append(False)
        for j,keywordSubList in enumerate(keywordList):
            for keyword in keywordSubList:
                if keyword in (str(code[i])).upper():
                    code[i]=codeRenew[j]
                    change[len(change)-1]=True
                    break
    return change

clean1=clean(pis['Code 1'])
clean2=clean(pis['Code 2'])
clean3=clean(pis['Code 3'])

print(pis["Code 1"])
print(clean1)

pis['clean1']=clean1
pis['clean2']=clean2
pis['clean3']=clean3

pis.to_excel('new.xlsx',index=False)

#FeelingBetter/Crime/SafetyPlan