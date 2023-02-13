
#angle 
a=int(input("Enter angle:"))

r= a*(3.14/180)

#base distance
d=int(input("Enter base distance:"))

n1=2
n2=4
n3=1
n4=3

l1=[]
l2=[]
l3=[]
l4=[]

sin=0
cos=0

for i in range(n1,200,4):
    l1.append(i)
for i in range(n2,200,4):
    l2.append(i)
for i in range(n3,200,4):
    l3.append(i)
for i in range(n4,200,4):
    l4.append(i)

def fact(x):
    for i in range(1,x):
        x*=i
    return x

for i in range(40):
    sin+=(r**(l3[i]))/(fact(l3[i]))
    sin-=(r**(l4[i]))/(fact(l4[i]))
    cos+=(r**(l2[i]))/(fact(l2[i]))
    cos-=(r**(l1[i]))/(fact(l1[i]))

cos+=1

tan=(sin/cos)

if a==0 or a==90:
    print("Invalid input")
else:
    print("height of pole=",d*tan)
    print("distance of pole=",d/cos)




