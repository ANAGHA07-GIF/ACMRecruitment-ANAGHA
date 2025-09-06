#ITERATIVE METHOD
s=input("Enter string:")
n = 0
for i in s:
    n += 1
rev = ""
for i in range(n - 1, -1, -1):  
    rev += s[i]
print(rev)

#RECURSIVE METHOD
s=input("Enter String:")
length = 0
for i in s:
    length += 1

rev = ""
while length > 0:
    rev += s[length - 1]
    length -= 1

print(rev)
