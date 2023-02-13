a=True
l=[]

while a==True :
    n=int(input())
    l.append(n)

    if n<=0:
        a=False

b=0
for i in l:
    b+=i

print("distance=",b)

east=0
north=0

#starting coordinates are (0,0)

for i in l:
    if i<=25:
        north+=i
    elif i>26 and i<50:
        north+=-i
    elif i>51 and i<75:
        east+=i
    elif i>75:
        east+=-i

print("displacement:",(((east*east)+(north*north))**0.5))

print("coordinates:",east,",",north)


