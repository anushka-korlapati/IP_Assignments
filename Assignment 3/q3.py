def netScore(fname):

    global m
    global top_5
    global random_list
    import random

    with open(fname,"r") as f:
        x=f.read().splitlines()

    sent=[]
    for i in x:
        sent.append(i)


    l=[]
    for i in x:
        i=i.split(' ')
        l.append(i)
    
    l2=l

    l6=[]
    for i in l2:
        for j in i :
            for k in j:
                if k in ".,;:":
                    l6.append(j)
                    break                

    l1=[]
    for i in l:
        for j in i:
            p=j.strip(".,;:)(/\[]{}")
            x=p.lower()
            l1.append(x)

    d={}
    for i in l1:
        count=0
        for j in l1:
            if i==j:
                count+=1
        d[i]=count

    
    # F1
    unique=len(d)
    total_words=0

    for k,v in d.items():
        total_words+=v

    f1_factor=unique/total_words

    # F2
    d = sorted(d.items(), key=lambda x:x[1],reverse = True)

    m=[]
    for i in range(0,5):
        m.append(d[i])

    random_list=[]
    for i in range(0,5):
        y=random.randint(0,len(d)-1)

    
        for j in range(len(d)):
            
            z=d[y][0]

            break
        random_list.append(z)


    top_5=[]
    for i in m:
        top_5.append(i[0])    

    top5=0

    for i in range(0,5):
        top5+=d[i][1]

    f2_factor=top5/total_words

    #F3
    sentences=[]
    for i in sent:
        a=i.split(".")
        for j in range(len(a)):
            if a[j]=="":
                a.remove(a[j])
        for k in a:
            sentences.append(k)

    word_s=[]
    for i in sentences:
        words=i.split(" ")
        word_s.append(words)

    sentences=[]
    for i in word_s:
        for j in range(len(i)):
            if i[j]=='':
                i.remove(i[j])
            sentences.append(i)
            break
    
    req_sentences=0

    for i in sentences:
        if len(i)<5 or len(i)>35:
            req_sentences+=1

    total_sentences=len(sentences)

    f3_factor=req_sentences/total_sentences

    # F4
    x=[]
    for i in l6:
        if i[-1] and i[-2] in ":;.,":
            x.append(i)

    frequency=len(x)

    f4_factor=frequency/total_words

    #F5
    if total_words>750:
        f5_factor=1
    else:
        f5_factor=0

    net_score= (4 + f1_factor*6 + f2_factor*6 -f3_factor - f4_factor - f5_factor)

    q=round(net_score,2)


    return q

choice="y"
while choice=="y":

    f=open("q3_out.txt", "w")
    fname=input("Enter name of file to evaluate:")
    x=netScore(fname)
    f.write(fname+'\n')
    f.write("Net Score:"+str(x)+'\n')
    f.write("Top 5 words:"+str(top_5)+"\n")
    f.write("Random words:"+str(random_list)+"\n")


    choice=input("Do you want to evaluate another file? (y/n) :")

    if choice=="y":
        
        fname=input("Enter name of file to evaluate:")
        x=netScore(fname)
        choice=input("Do you want to evaluate another file? (y/n) :")
        f.write(fname+'\n')
        f.write("Net Score:"+str(x)+'\n')
        f.write("Top 5 words:"+str(top_5)+"\n")
        f.write("Random words:"+str(random_list)+"\n")
    
    else:
        
        f.close()
        break

