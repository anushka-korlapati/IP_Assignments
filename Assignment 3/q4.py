import time
fname="q4,q5_in.txt"
with open(fname,"r") as f:
    x=f.read().splitlines()

weights=[30,15,30,25]

marks=[]
for i in x:
    a=i.split(',')
    for j in range(len(a)):
        a[j]=int(a[j])
    marks.append(a)

class Course():

    def __init__(self,marks,weights):

        self.marks= marks
        self.weights= weights
        self.gradeA=[]
        self.gradeB=[]
        self.gradeC=[]
        self.gradeD=[]
        self.d={}
        self.A,self.B,self.C,self.D = 0,0,0,0

    def percentages(self):

        self.d={}
        for i in marks:
            total_marks=0
            for j in range(1,len(i)):
                total_marks+=(i[j]/100*weights[j-1])
            self.d[i[0]]=round(total_marks,2)

    def grade_lists(self):

        for k,v in self.d.items():

            if v<=82 and v>78:
                self.gradeA.append(v)

            elif v<67 and v>=63:
                self.gradeB.append(v)

            elif v<=52 and v>=48:
                self.gradeC.append(v)

            elif v<=42 and v>=38:
                self.gradeD.append(v)

        self.gradeA.sort()
        self.gradeB.sort()
        self.gradeC.sort()
        self.gradeD.sort()

    def newCutoff(l):
        dif=[]
        for i in range(0,len(l)-1):
            diff=l[i+1]-l[i]
            dif.append(abs(round(diff,3)))

        x=max(dif)
        index=dif.index(x)
        new_cutoff=round((l[index]+l[index+1])/2,3)
        return new_cutoff
    
    def cut_offs(self):
        if self.gradeA==[] or len(self.gradeA)==1:
            self.A+=80
            # print(self.A)
        else:
            self.A+=Course.newCutoff(self.gradeA)
            # print(self.A)

        if self.gradeB==[]  or len(self.gradeB)==1:
            self.B+=65
            # print(self.B)
        else:
            self.B+=Course.newCutoff(self.gradeB)
            # print(self.B)

        if len(self.gradeC)==0 or len(self.gradeC)==1:
            self.C+=50
            # print(self.C)
        else:
            self.C+=Course.newCutoff(self.gradeC)
            # print(self.C)

        if self.gradeD==[] or len(self.gradeD)==1:
            self.D+=40
            # print(self.D)
        else:
            self.D+=Course.newCutoff(self.gradeD)
            # print(self.D)


class Grades(Course):
    def up_policy(self):
        Course.percentages(self)
        Course.grade_lists(self)
        Course.cut_offs(self)
        policy=[self.A,self.B,self.C,self.D]
        return policy

    def grading(self):
        Course.percentages(self)
        Course.grade_lists(self)
        Course.cut_offs(self)
        A_count=0
        B_count=0
        C_count=0
        D_count=0
        F_count=0
        for k,v in self.d.items():
            if v>=self.A:
                self.d[k]=str(v)+", A"
                A_count+=1
            elif v<self.A and v>=self.B:
                self.d[k]=str(v)+", B"
                B_count+=1
            elif v<self.B and v>=self.C:
                self.d[k]=str(v)+", C"
                C_count+=1
            elif v<self.C and v>=self.D:
                self.d[k]=str(v)+", D"
                D_count+=1
            elif v<self.D:
                self.d[k]=str(v)+", F"
                F_count+=1

        return self.d


def Main():
    global pol
    global reqx

    v=Course(marks,weights)
    w=Grades(marks,weights)
    v.percentages()
    v.grade_lists()
    v.cut_offs()
    pol=(w.up_policy())
    reqx=(w.grading())

Main()
    
def Menu():
    
    assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
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
            print("Updated Grade cutoffs :",pol)

        elif choice=='2':
            # start=time.time()
            # count=0
            f=open("q4_output.txt","w")
            for k, v in reqx.items():
                count+=1
                f.write(str(k)+":"+' '+str(v)+'\n')
            f.close()
            # end=time.time()
            # print(end-start)
            # print(count)

        elif choice=='3':
            start=time.time()
            count=0
            roll_no=int(input("Enter student roll no:"))
            
            for k, v in reqx.items():
                count+=1
                if k==roll_no:
                    print(str(k),":",str(v))
            end=time.time()
            print(end-start)
            print(count)


        elif choice=='':
            print('THANK YOU')
            break

        else:
            print('Invalid choice!')
        
Menu()
