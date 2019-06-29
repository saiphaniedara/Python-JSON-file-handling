import json
file=open("F6_Week5.json")
info=json.load(file)
file.close()
td=list()
for a in info:
    for b in a:
        if b==a[0]:
           dow=b['dow']
        if b==a[1]:
           time=b['time']
        if b==a[2]:
           c=b['conference-categories-count']
           count=c['Small']+c['Phone Booth']+c['Medium']+c['Large']
           td.append((dow,time,count))
x=('Monday','Tuesday','Wednesday','Thursday','Friday')
z=dict()
i=0
for va in x:
    cou=0
    for a in td:
        if a[0]==va:
            z[a[1]]=a[2]
            cou+=1
            if cou==8:
                print(va,'==>',z)
