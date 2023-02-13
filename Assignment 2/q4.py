list=["abuse", "adult", "anger", "apple", "award", "beach", "birth", "block","chain", "blood",
"drama","dream", "dress", "drink","drive", "earth", "entry", "error", "event", "faith", 
"admit", "adopt", "allow", "agree", "avoid", "blame", "chief", "chair", "child", "cream", 
"bread", "brain", "blind", "cross", "dream", "coast", "enemy", "dance", "force", "heart",
"group", "hotel", "judge", "knife", "level", "light", "metal", "money", "noise", "party"]

#Selected word
import random
a=random.randint(0,49)
word=list[a]

#List of letters of selected word
l=[]
for i in word:
    l.append(i)

for f in range(6):
    #Guessed word
    guess=input("Enter your guess:")

    if len(guess)!=5:#If the word is not five letters
        print("Enter a five letter word")

    else:
        #List of letters of guessed word
        s=[]
        for i in guess:
            s.append(i)

        #Finding letters that are in correct position in the guess
        newlist=[]#List that contains letters that are in correct position

        for a,b in zip(l,s):
            if a==b:
                newlist.append(b)

        #Finding letters that are in the word but not in correct position        
        nw=[]#List that contains letters that are in wrong position

        for i in s:
            if i not in newlist:
                if i in l:
                    nw.append(i)

        
        for i in range(0,5):
            if l[i]==s[i]:
                print(l[i],end="")
            else:
                print("-",end="")

        print()

        if nw!=[]:    
            print("Letters that are not in correct position:")
            for i in nw:
                print(i,end=" ")

        print()

        if guess==word:
            print("Correct word!")
            break

print('Correct word :',word)