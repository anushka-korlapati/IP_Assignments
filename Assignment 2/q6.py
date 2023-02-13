wts = [(10, 5), (20, 5), (100, 15), (40, 10), (100, 35), (100, 30)]

weightage=[]
for i in range(len(wts)):

    a=wts[i][0]/wts[i][1]
    a=round(a,2)
    weightage.append(a)

#opening file
fname="Ipmarks.txt"
l=[]
with open(fname,"r") as f:
    l=f.read().splitlines() #list of everything in l

l1=[]
for i in l:
    x=i.split(",")
    l1.append(x)

list=[]
for i in l1:
    for j in i:
        d=j.strip()
        list.append(d)

for i in l1:
    for j in range(1,len(i)):
        i[j]=int(i[j])


f=open("IPgrades.txt","w")

#Calculating Grades
for i in l1:
    totalmarks=0
    for j in range(1,len(i)):
        totalmarks+=i[j]/weightage[j-1]
        totalmarks=round(totalmarks,2)
    if totalmarks>80:
        grade="A"
    elif totalmarks>70:
        grade="A-"
    elif totalmarks>60:
        grade="B"
    elif totalmarks>50:
        grade="B-"
    elif totalmarks>40:
        grade="C"
    elif totalmarks>35:
        grade="C-"
    elif totalmarks>30:
        grade="D"
    elif totalmarks<30:
        grade="F"
    f.write(i[0]+", "+str(totalmarks)+", "+grade+"\n")

