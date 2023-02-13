import math

#starting time
a=int(input("Enter starting time:"))

#ending time
b=int(input("Enter starting time:"))

#time
t=b-a

#velocity

z=0
v=0

while a<b:
    v+= (2000*math.log(140000/(140000-2100*a)))-(9.8*a)
    a+=0.25
    z+=1


d=(v*t)/z
print("distance",d)







