#Student Details Input
l = []
credits = []
grades = []
TotalCredits = 0
print("Enter course code, no. of credits and grade:")
cond=True
while True:
    x=list(map(str,input().split()))
    if len(x)!=3:
        break
    #Checking if improper course code
    cond1=True
    for i in range(0,len(x),3):
        if x[i].isalnum():
            if x[i].isdigit():
                cond1=False
            for j in x[i]:
                if j.isalpha():
                    if j.isupper():
                        pass
                    else:
                        cond1=False
        if x[i][-1].isalpha():
            cond1=False

    #Checking if improper course credits
    cond2=False
    if x[1] in "124":
        cond2=True

    #Checking if improper course grades
    cond3=True
    if x[2] in ["A+","A","A-","B","B-","C","C-","D","D-","F"]:
            cond3=True
    else:
        False
    if cond1==True and cond2==True and cond3==True:
        l+=x
    if cond1==True: #Correct course code
        
        if cond2==True: #Correct course credits
            
            #Calculating Total Credits
            for i in range(1,len(x),3):
                TotalCredits+= int(x[i]) #Adding number of credits

            #Credits
            for i in range(1,len(x),3):
                credits.append(int(x[i]))
            
            if cond3==True:

                #Calculating Grades
                for i in range(2,len(x),3):
                    if x[i]=="A+":
                        grade=10
                        cond3=True
                    elif x[i]=="A":
                        cond3=True
                        grade=10
                    elif x[i]=="A-":
                        cond3=True
                        grade=9
                    elif x[i]=="B":
                        cond3=True
                        grade=8
                    elif x[i]=="B-":
                        cond3=True
                        grade=7
                    elif x[i]=="C":
                        cond3=True
                        grade=6
                    elif x[i]=="D":
                        cond3=True
                        grade=5
                    elif x[i]=="E":
                        cond3=True
                        grade=4
                    elif x[i]=="F":
                        cond3=True
                        grade=2

                    else:
                        cond3=False
                        print("Improper course grade")
                    
                    if cond3==True:
                        grades.append(grade)

                
    elif cond1==False:
        print("Improper course code")

    elif cond2==False:
        print("Improper course credits")

    elif cond3==False:
        print("Improper course grade")


#SGPA
sumSgpa=0
sgpa = [credits[i]*grades[i] for i in range(len(grades))]

for i in sgpa:
    sumSgpa+=i

SGPA=sumSgpa/TotalCredits

#Transcript
print("TRANSCRIPT:")
for i in range(0,len(l),3):
    print(l[i],":",end="") #CourseNo
    print(l[i+2]) #Grade

#SGPA
finSgpa=round(SGPA,2)
print()
print("SGPA:",finSgpa)