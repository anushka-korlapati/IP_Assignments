cx=int(input("Cx:"))
cy=int(input("Cy:"))

M=[[cx,0,0],
   [0,cy,0],
   [0,0,1] ]

a=True
l=[]
x=list(map(int,input().split()))
l.append(x)
while a==True:
    if x==[]:
        break
    if x!=[]:
        x=list(map(int,input().split()))
        if x==[]:
            break
        if len(x)!=2:
            a=False
        l.append(x)
         
for i in l:
    i.append(1)


result = [[sum(a * b for a, b in zip(M_row, l_col))
                        for l_col in zip(*M)]
                                for M_row in l]


for j in result:
    print(j[0],j[1])