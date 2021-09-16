hzsrt=input()
hzl=len(hzsrt)
scount=input()
wlist=[]
for i in range(int(scount)):
    tempstr=input()
    cmpstr=tempstr[0:hzl]
    if cmpstr==hzstr:
        wlist.append(tempstr)
wlist.sort()#排序
for word in wlist:
    print(word)