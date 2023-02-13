fname="sorted_data.txt"
fname1="q2_output.txt"

with open(fname,"r") as f:
    x=f.read().splitlines()

l1=[]
for i in x:
    l=[]
    l.append(i)
    l1.append(l)

l2=[]   
for i in l1:
    for j in i:
        a=j.split(",")
        l2.append(a)

sorted(l2, key=lambda x:x[3])

ta_list=[]
for i in l2:
    ta_list.append(i[0])
crossing_list=[]
for i in l2:
    crossing_list.append(i[1].strip())
gate_list=[]
for i in l2:
    if i[2]==' Gate number':
        gate_list.append((i[2]).strip())
    else:
        gate_list.append(int(i[2]))

time_list=[]
for i in l2:
    time_list.append(i[3].strip())

d = {}
for i in range(0,len(ta_list)):
    d[ta_list[i]] = {}

for i in range(0,len(ta_list)):
    d1={}
    d1['Crossing']=crossing_list[i]
    d1['Gate number']=gate_list[i]
    d1['Time']=time_list[i]
    g=[]
    for k,v in d.items():
        
        if ta_list[i]==k:
            g.extend(v)
            g.append(d1)
            d[ta_list[i]]=g


# Part one
def part_one():
    student_name=input("Enter student name:")
    time=input("Enter current time:")
    l=[]
    m=[]

    f= open(fname1,"w")
    for k,v in d.items():
            if student_name==k:  
                f.write("Student Details:"+'\n')
                f.write(str(k)+'\n')
                x=v

    if type(x)==list:
        for i in x:
            f.write(str(i)+'\n')
        for i in x:
            for j in i.values():
                l.append(j)

    else:
        f.write(str(x)+'\n')
        for i in x.values():
            m.append(i)

    f.close()

    if len(l)>0:
        if l[-1]<=time:
            print("The student is in campus")
        else:
            print("The student is not in campus")

    else:
        if m[-1]<=time:
            print("The student is in campus")
        else:
            print("The student is not in campus")


# Part two
def part_two():
    f=open(fname1,"w")

    start_time=input("Enter start time: ")
    end_time=input("Enter end time: ")

    for k,v in d.items():
        if type(v)==list:
            for a in v:
                for i,j in a.items():
                    if i=="Time":
                        if j>=start_time and j<=end_time:
                            f.write(str(k)+str(a)+'\n')

        else:
            for i,j in v.items():
                if i=="Time":
                    if j>=start_time and j<=end_time:
                        f.write(str(k)+str(v)+'\n')

    f.close()

# Part three
def part_three():
    
    gate=int(input("Enter gate number(1/3/5) :"))
    enter=0
    exit=0
    ent_exit_list=[]

    for j,v in d.items():
        if type(v)==list:
            for l in v:
                for f,g in l.items():
                    if f=="Gate number":
                        if g==gate:
                            # print(j,l)
                            ent_exit_list.append(l)
        else:
            for k,i in v.items():
                if k=="Gate number":
                    if i==gate:
                        # print(j,v)
                        ent_exit_list.append(v)

    for i in ent_exit_list:
        for k,v in i.items():
            if k=="Crossing":
                if v=="ENTER":
                    enter+=1
                elif v=="EXIT":
                    exit+=1

    print("The no of students that have entered through this gate are:",enter)
    print("The no of students that have exited through this gate are:",exit)

def Menu():
    print("1.student details and records at current time")
    print("2.student data for start time and end time")
    print("3.gate details")
    print("4.exit")

    while True:
        choice=int(input("Enter your choice:"))

        if choice==1:
            part_one()
        
        elif choice==2:
            part_two()

        elif choice==3:
            part_three()

        elif choice==4:
            break

Menu()



    