import math
a=10
b=1.05
c=1
d=1.06

price=1

def demand(price):
     Demand=a -(b*price)
     return math.e**(Demand)

def supply(price):
    Supply=c + (d*price)
    return math.e**(Supply)


x = demand(price)
y = supply(price)

while y<x:
    price+=(5/100)*price
    
    x = demand(price)
    y = supply(price)

print(price)
print("demand:",x)
print("supply:",y)
