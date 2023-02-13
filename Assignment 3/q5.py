assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
import time

fname="q4,q5_in.txt"

with open(fname,"r") as f:
    x=f.read().splitlines()

l2=[]
for i in x:
    a=i.split(",")
    l2.append(a)


for i in l2:
    for j in range(1,len(i)):
        i[j]=int(i[j])

l1=[]
for i in l2:
    l1.append(i)

for i in l2:
    for j in range(1,len(i)):
        i[j]=(i[j])/100

weightage=[]

for i in assessments:
    weightage.append(i[1])


for i in l2:
    for j in range(1,len(i)):
        i[j]=round((i[j]*weightage[j-1]),2)

d={}
        
for i in l2:
    
    total_marks=0
    for j in range(1,len(i)):
        total_marks+=i[j]
    d[i[0]]=total_marks

gradeA=[]
gradeB=[]
gradeC=[]
gradeD=[]

for k,v in d.items():

    if v<=82 and v>78:
        gradeA.append(v)

    elif v<67 and v>=63:
        gradeB.append(v)

    elif v<=52 and v>=48:
        gradeC.append(v)

    elif v<=42 and v>=38:
        gradeD.append(v)

gradeA.sort()
gradeB.sort()
gradeC.sort()
gradeD.sort()

def newCutoff(l):

    dif=[]
    for i in range(0,len(l)-1):
        diff=l[i+1]-l[i]
        dif.append(abs(round(diff,3)))

    x=max(dif)
    index=dif.index(x)
    new_cutoff=round((l[index]+l[index+1])/2,3)
        
    return new_cutoff

if gradeA==[] or len(gradeA)==1:
    A=80
else:
    A=newCutoff(gradeA)

if gradeB==[]  or len(gradeB)==1:
    B=65    
else:
    B=newCutoff(gradeB)

if gradeC==[] or len(gradeC)==1:
    C=50
else:
    C=newCutoff(gradeC)

if gradeD==[] or len(gradeD)==1:
    D=40
else:
    D=newCutoff(gradeD)

A_count=0
B_count=0
C_count=0
D_count=0
F_count=0

up_policy=[A,B,C,D]
print(up_policy)

for k,v in d.items():
    if v>=A:
        d[k]=str(v)+", A"
        A_count+=1
    elif v<A and v>=B:
        d[k]=str(v)+", B"
        B_count+=1
    elif v<B and v>=C:
        d[k]=str(v)+", C"
        C_count+=1
    elif v<C and v>=D:
        d[k]=str(v)+", D"
        D_count+=1
    elif v<D:
        d[k]=str(v)+", F"
        F_count+=1

grade_count={}
grade_count['A']=A_count
grade_count['B']=B_count
grade_count['C']=C_count
grade_count['D']=D_count
grade_count['F']=F_count

for k, v in d.items():
    with open("student_grades.txt","a") as f:
        f.write(k+":" + ' '+v+'\n')

def Menu():
    print("1. Summary of Course")
    print("2. Get grades of all students ")
    print("3. Search for a student's Records ")

    course=input("Enter course name: ")
    credits=input("Enter course credits: ")

    while True:
        choice=input("Enter your choice: ")
        if choice=='1':
            print("Course Name           :",course)
            print("Course credits        :",credits)
            print("Assessments           :",assessments)
            print("Updated Grade cutoffs :",up_policy)
            print("Grades                :",grade_count)

        elif choice=='2':
            start=time.time()
            counter=0
            f=open("q5_output","w")
            for k, v in d.items():
                counter+=1    
                f.write(k+":"+' '+v+'\n')
            end=time.time()
            f.close()
            # print(end-start)
            # print(counter)


        elif choice=='3':
            start=time.time()
            counter=0
            roll_no=input("Enter student roll no:")
            for k, v in d.items():
                counter+=1
                if k==roll_no:
                    print(k,":",v)
            end=time.time()
            # print(end-start)
            # print(counter)

        elif choice=='':
            print('THANK YOU!!!')
            break

        else:
            print('Invalid choice!')
        
Menu()
