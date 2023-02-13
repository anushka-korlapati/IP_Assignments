#equation
#x**3-10.5*x**2+34.5*x-35

def fx(x):
    return (x**3)-(10.5*x**2)+(34.5*x)-35

def f2x(x):
    return 3*(x**2)-(2*10.5*x)+(34.5)
    

x=int(input()) #initial value

a=fx(x)/f2x(x)
condition=abs(a)>0.00001

while condition==True:
    a=fx(x)/f2x(x)
    x = x-a
    if abs(a)<=0.00001:
        break
print(x)








