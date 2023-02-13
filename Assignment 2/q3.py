d={}
fname="Yearbook.txt"
with open(fname,"r") as f:
    l=f.read().splitlines()
    #print(l)

students=[]
for i in l:
    if i=="":
        pass
    else:
        if i[-1]==":":
            students.append(i)

print(students)

noOfStudents=len(students)

#print(noOfStudents)

l1=[i for i in l if i not in students and i!=""]

l2=[]
for j in l1:
    l2.append(int(j[-1]))


noOfsigns=[]
i=0
while i<noOfStudents:
    count=0
    for j in range(noOfStudents-1):
        count+=l2[0]
        l2.pop(0)
    noOfsigns.append(count)
    i+=1

noOfsigns=[2,2,1,0]


Max=max(noOfsigns)
Min=min(noOfsigns)


for i in range(0,len(students)):
    d[students[i]]=noOfsigns[i]

for keys,values in d.items():
    if values == Max:
        print("Maximum signs is :",keys,values)
    elif values == Min:
        print("Minimum sign of student is :",keys,values)

