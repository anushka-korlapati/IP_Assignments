fname="pages.txt"
url_list = []
importance_list = []
url_text_list = []

with open(fname,"r") as f:
    l=f.read().splitlines()

l1=[]
for i in l:
    y=i.split(":")
    l1.append(y)

l2=[]
for i in l1:
    l2.append(i[0])


init_importance=[]
urls=[]
for i in l2:
    url,importance=i.split(",")
    init_importance.append(importance)
    urls.append(url)


checkForUrl=[]
for i in l:
    x,y=i.split(":")
    checkForUrl.append(y)

l = []
for i in checkForUrl:
    l1 = []
    for j in urls:
        if j in i:
            l1.append(j)
    l.append(l1)

dict1 = {}
for i in range(len(urls)):
    dict1[urls[i]] = {
        'Init Importance': float(init_importance[i]),
        'Importance': 0.0,
        'Url': l[i]
    }


for p in dict1.values():
    calc = p['Init Importance']/len(p['Url'])
    for i in p['Url']:
        dict1[i]['Importance'] += calc


sorted_list = sorted(dict1.items(), key=lambda x:x[1]['Importance'], reverse=True)
for i in sorted_list:
    print(i[0]+': '+str(i[1]['Importance']))