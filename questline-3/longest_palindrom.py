y=input()
x=y.split()
l=[]
for i in x:
    if i==i[::-1]:
        l.append(i)
largest=len(l[0])
for i in range(0,len(l)):
               j=len(l[i])
               if j>largest:
                   k=i
                   largest=j
print(largest)
print(l[k])


