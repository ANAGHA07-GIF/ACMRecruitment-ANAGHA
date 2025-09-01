x=input()
y=x.split()
l=[]
for i in y:
    if i not in l:
        l.append(i)
for k in l:
    a=y.count(k)
    print(k,'=',a)
