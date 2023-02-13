
#Menu 
Menu=[("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
print("Menu:")
print("1. Samosa: 15")
print("2. Idli: 30")
print("3. Maggie: 50")
print("4. Dosa: 70")
print("5. Tea: 10")
print("6. Coffee: 20")
print("7. Sandwich: 35")
print("8. ColdDrink: 25")
print()

#User Order
print("Enter item no and quantity:")
a=True
l=[]
while a==True:
    
    x=list(map(int,input().split()))
    if len(x)!=2:
        a=False
    l+=x 

#Order Cost 
print("BILL:")
TotalCost=0
TotalItems=0
for i in range(0,len(l),2):
    print(Menu[l[i]-1][0],end=" ")
    print(l[i+1],end=" ")
    print("Rs."+str((int(Menu[l[i]-1][1])*int(l[i+1]))))
    TotalCost+=int(Menu[l[i]-1][1])*int(l[i+1])
    TotalItems+=int(l[i+1])

#Order Summary
print("TOTAL,",TotalItems,"items, Rs",TotalCost)