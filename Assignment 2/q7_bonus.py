
import json

def Menu():
    print("1.insert a new entry")
    print("2.delete an entry ")
    print("3.find all matching entries given a partial name")
    print("4.find the entry with a phone number or email")
    print("5.exit")
    print("6.merge dictionary")

    fname="addressbook.txt"
    with open(fname,"r") as f:
        new_d2=json.load(f)
    if new_d2=={}:
        d2={}
        pass
    else:
        d2=new_d2
    while True:
        ch=int(input("Enter your choice:"))

        if len(str(ch))!=1:
            print("enter a valid choice")

        elif ch==1:
            
            newd2= newEntry(d2)
            with open("addressbook.txt","r") as f:
                new_d2=json.load(f)

            if newd2=={}:
                d2=newd2
                pass
            else:
                d2={**new_d2,**newd2}

            
        elif ch==2:

            deleteEntry(d2)

        elif ch==3:
            partialName(d2)
            
        elif ch==4:
            findEntry(d2)

        elif ch==5:
            with open("addressbook.txt","w") as f:
                json.dump(d2,f)
            break

        elif ch==6:

            d2=merge_dict(d2)
            

def newEntry(d2):

    name=input("Enter name: ")
    address=input("Enter address: ")
    phone=input("Enter phone no: ")
    email=input("Enter email: ")

    d1={}
    temp=[]

    d1['Address']=address
    d1['Phone']=phone
    d1['Email']=email
    
    if name in list(d2.keys()):
        temp.append(d2[name])
        temp.append(d1)
        d2[name]=temp

    return d2


def deleteEntry(d2):

    delName=input("Enter name of person to delete: ")
    if type(d2[delName])==list:
        if len(d2[delName])>1:
            d2[delName].pop(-1)
        else:
            del d2[delName]

    else:        
        del d2[delName]

    return d2

def partialName(d2):

    partial=input("Enter partial name: ")

    for i in d2.keys():
        if partial.lower() in i.lower():
            print(i)
            print(d2[i])

def findEntry(d2):

    match=input("Enter phone number or email: ")

    for k,i in d2.items():
        for j in i.values():
            if j==match:
                print(k,i)

def merge_dict(d2):
    with open('friendaddressbook.txt') as g:
        friend_dict= json.load(g)
    d2.update(friend_dict)
    return d2


Menu()