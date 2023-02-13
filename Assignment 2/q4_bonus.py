import requests

def dictionary(word_id):

    app_id  = "05ce9103"
    app_key  = "7a05b6ff3caaea10db41405911b556d9"
    endpoint = "entries"
    language_code ="en-us"
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
    if word_id in r.text:
        return True
    else:
        return False

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

attempts=0
while attempts<6:
    #Guessed word
    guess=input("Enter your guess:")

    x=dictionary(guess)

    if x==False:
        print("Word is not in the dictionary")
        attempts+=-1

    else:
        attempts+=1

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




