s=input()
k=int(input())
y=len(s)
direction=input("Enter left or right")
if direction.upper()=="RIGHT":
    for i in range(k):
        s=s[y-1]+s[0:y-1]
        sum=0
    for i in range(y):
        a=int(s[i])*2**(y-1-i)
        sum=sum+a
    print(sum)
else:
    for i in range(k):
        s=s[1:y]+s[0]
        sum=0
    for i in range(y):
        a=int(s[i])*2**(y-1-i)
        sum=sum+a
    print(sum)
    

    
