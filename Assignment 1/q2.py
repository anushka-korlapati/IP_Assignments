


m=10
#m=0
#m=20
x1=0

for i in range(0,400):
    x2a=120-2*x1
    x2b=200-4*x1
    if x2a==x2b:
        print("x1:",x1,",x2:",x2a)
        break
    else:
        x1+=1


x1=(90*m)+(100*(x1-m))

x2a=(25*m)+(30*(x2a-m))

print("maximum profit:",x1+x2a)






    
