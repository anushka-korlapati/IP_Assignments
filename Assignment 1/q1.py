
#works upto number 9,99,999

n=input("Enter a number:")
l=[]

z=int(n)

for i in n:
    l.append(i)

l.reverse()

a=["one","two","three","four","five","six","seven","eight","nine"]
b=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
c=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

if n=='0' and len(l)==1:
    print("zero")

elif z>9 and z<20:
    print(c[z-10])
    
elif n!='0'and len(l)==1:
    ones=int(l[0])
    print(a[ones-1])

elif len(l)==2 and l[1]=='0':
    tens=int(l[1])
    print(b[tens-2])

elif len(l)==2 and l[1]!='0':
    tens=int(l[1])
    ones=int(l[0])

    print(b[tens-2],end='')
    print("-",end='')
    print(a[ones-1])

elif len(l)==3 and l[1]=="0" and l[0]=="0":
    hundreds=int(l[2])
    print(a[hundreds-1],"hundred")

elif len(l)==3 and l[1]!="0" and l[0]=="0":
    hundreds=int(l[2])
    tens=int(l[1])
    print(a[hundreds-1],"hundred",end=" ")
    print(b[tens-2])

elif len(l)==3 and l[1]!="0" and l[0]!="0":
    hundreds=int(l[2])
    tens=int(l[1])
    ones=int(l[0])
    print(a[hundreds-1],"hundred and",end=" ")
    print(b[tens-2],end="")
    print("-"+a[ones-1])
    
elif len(l)==4 and l[2]=="0" and l[1]=="0" and l[0]=="0":
    thousands=int(l[3])
    print(a[thousands-1],"thousand")

elif len(l)==4 and l[2]=="0" and l[1]=="0" and l[0]=="0":
    thousands=int(l[3])
    print(a[thousands-1],"thousand",end="")

elif len(l)==4 and l[2]=="0" and l[1]=="0" and l[0]=="0":
    thousands=int(l[3])
    print(a[thousands-1],"thousand",end="")

elif len(l)==4 and l[2]!="0" and l[1]=="0" and l[0]=="0":
    thousands=int(l[3])
    hundreds=int(l[2])   
    print(a[thousands-1],"thousand",end="")
    print(a[hundreds-1],"hundred")

elif len(l)==4 and l[2]!="0" and l[1]=="0" and l[0]=="0":
    thousands=int(l[3])
    hundreds=int(l[2])   
    print(a[thousands-1],"thousand",end="")
    print(a[hundreds-1],"hundred")

elif len(l)==4 and l[2]!="0" and l[1]!="0" and l[0]=="0":
    thousands=int(l[3])
    hundreds=int(l[2])   
    tens=int(l[1])
    print(a[thousands-1],"thousand",end="")
    print(a[hundreds-1],"hundred",end=" ")
    print(b[tens-2])

elif len(l)==4 and l[2]!="0" and l[1]!="0" and l[0]!="0":
    thousands=int(l[3])
    hundreds=int(l[2])   
    tens=int(l[1])
    ones=int(l[0])
    print(a[thousands-1],"thousand ",end="")
    print(a[hundreds-1],"hundred and",end=" ")
    print(b[tens-2],end="")
    print("-"+a[ones-1])

elif len(l)==5 and z>9999 and z<=19999:
    if z==10000:
        print("ten thousands")
    elif z>10000 and z<11000 and l[2]!=0 and l[1]==0 and l[0]==0:
        print("ten thousand",end="")
        hundreds=int(l[2])   
        print(a[hundreds-1],"hundred")

    elif z>10000 and z<11000 and l[2]!=0 and l[1]!=0 and l[0]==0:
        print("ten thousand",end="")
        hundreds=int(l[2])   
        tens=int(l[1])
        print(a[hundreds-1],"hundred",end=" ")
        print(b[tens-2])

    elif z>10000 and z<11000 and l[2]!=0 and l[1]!=0 and l[0]!=0:
        print("ten thousand ",end="")
        hundreds=int(l[2])   
        tens=int(l[1])
        ones=int(l[0])
        print(a[hundreds-1],"hundred",end=" ")
        print(b[tens-2],end="")
        print("-"+a[ones-1])    
    
    elif z>10999 and l[2]=="0" and l[1]=="0" and l[0]=="0":
        tenthousands=(int(l[4])*10+int(l[3]))
        print(c[tenthousands-10], "thousands")

    elif z>10999 and l[2]!="0" and l[1]=="0" and l[0]=="0":
        tenthousands=(int(l[4])*10+int(l[3]))
        hundreds=int(l[2])
        print(c[tenthousands-10], "thousands ",end="")
        print(a[hundreds-1],"hundred",end=" ")

    elif z>10999 and l[2]!="0" and l[1]!="0" and l[0]=="0":
        tenthousands=(int(l[4])*10+int(l[3]))
        hundreds=int(l[2])
        tens=int(l[1])
        print(c[tenthousands-10], "thousands ",end="")
        print(a[hundreds-1],"hundred",end=" ")
        print(b[tens-2],end="")

    elif z>10999 and l[2]!="0" and l[1]!="0" and l[0]!="0":
        tenthousands=(int(l[4])*10+int(l[3]))
        hundreds=int(l[2])
        tens=int(l[1])
        ones=int(l[0])
        print(c[tenthousands-10], "thousands ",end="")
        print(a[hundreds-1],"hundred",end=" ")
        print(b[tens-2],end="")
        print("-"+a[ones-1]) 


elif len(l)==5 and z>19999:
    if l[3]=="0" and l[2]=="0" and l[1]=="0" and l[0]=="0":
        tenthousands=int(l[4])
        print(b[tenthousands-2],"thousand")
    elif l[3]!="0" and l[2]=="0" and l[1]=="0" and l[0]=="0":
        tenthousands=int(l[4])
        thousands=int(l[3])
        print(b[tenthousands-2]+"-",end="")
        print(a[thousands-1],"thousand" )
    elif l[3]!="0" and l[2]!="0" and l[1]=="0" and l[0]=="0":
        tenthousands=int(l[4])
        thousands=int(l[3])
        hundreds=int(l[2])
        print(b[tenthousands-2]+"-",end="")
        print(a[thousands-1],"thousand ",end="")
        print(a[hundreds-1],"hundred",)

    elif l[3]!="0" and l[2]!="0" and l[1]!="0" and l[0]=="0":
        tenthousands=int(l[4])
        thousands=int(l[3])
        hundreds=int(l[2])
        tens=int(l[1])
        print(b[tenthousands-2]+"-",end="")
        print(a[thousands-1],"thousand ",end="")
        print(a[hundreds-1],"hundred ",end="")
        print(b[tens-2],end="")

    elif l[3]!="0" and l[2]!="0" and l[1]!="0" and l[0]=="0":
        tenthousands=int(l[4])
        thousands=int(l[3])
        hundreds=int(l[2])
        tens=int(l[1])
        print(b[tenthousands-2]+"-",end="")
        print(a[thousands-1],"thousand ",end="")
        print(a[hundreds-1],"hundred ",end="")
        print(b[tens-2],end="")

    elif l[3]!="0" and l[2]!="0" and l[1]!="0" and l[0]!="0":
        tenthousands=int(l[4])
        thousands=int(l[3])
        hundreds=int(l[2])
        tens=int(l[1])
        ones=int(l[0])
        print(b[tenthousands-2]+"-",end="")
        print(a[thousands-1],"thousand ",end="")
        print(a[hundreds-1],"hundred ",end="")
        print(b[tens-2],end="")
        print("-"+a[ones-1])

elif len(l)==6 and l[4]=="0" and l[3]=="0" and l[2]=="0" and l[1]=="0" and l[0]=="0":
    lakhs=int(l[5])
    print(a[lakhs-1],"lakh")

elif len(l)==6 and l[4]!="0" and l[3]=="0" and l[2]=="0" and l[1]=="0" and l[0]=="0":
    lakhs=int(l[5])
    tenthousands=int(l[4])
    print(a[lakhs-1],"lakh ",end="")
    print(b[tenthousands-2],"thousand")

elif len(l)==6 and l[4]!="0" and l[3]!="0" and l[2]=="0" and l[1]=="0" and l[0]=="0":
    lakhs=int(l[5])
    tenthousands=int(l[4])
    thousands=int(l[3])
    print(a[lakhs-1],"lakh ",end="")
    print(b[tenthousands-2],end="")
    print("-"+a[thousands-1],"thousand" )

elif len(l)==6 and l[4]!="0" and l[3]!="0" and l[2]!="0" and l[1]=="0" and l[0]=="0":
    lakhs=int(l[5])
    tenthousands=int(l[4])
    thousands=int(l[3])
    hundreds=int(l[2])
    print(a[lakhs-1],"lakh ",end="")
    print(b[tenthousands-2],end="")
    print("-"+a[thousands-1],"thousand",end=" ")
    print(a[hundreds-1],"hundred ",end="")


elif len(l)==6 and l[4]!="0" and l[3]!="0" and l[2]!="0" and l[1]!="0" and l[0]=="0":
    lakhs=int(l[5])
    tenthousands=int(l[4])
    thousands=int(l[3])
    hundreds=int(l[2])
    tens=int(l[1])

    print(a[lakhs-1],"lakh ",end="")
    print(b[tenthousands-2],end="")
    print("-"+a[thousands-1],"thousand",end=" ")
    print(a[hundreds-1],"hundred ",end="")
    print(b[tens-2],end="")
    

elif len(l)==6 and l[4]!="0" and l[3]!="0" and l[2]!="0" and l[1]!="0" and l[0]!="0":
    lakhs=int(l[5])
    tenthousands=int(l[4])
    thousands=int(l[3])
    hundreds=int(l[2])
    tens=int(l[1])
    ones=int(l[0])
    print(a[lakhs-1],"lakh ",end="")
    print(b[tenthousands-2],end="")
    print("-"+a[thousands-1],"thousand",end=" ")
    print(a[hundreds-1],"hundred ",end="")
    print(b[tens-2],end="")
    print("-"+a[ones-1])





