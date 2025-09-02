s=list(input().split())
for y in s:
    temp=y
    i=int(y)
    st=''
    while i>0:
        n=i%2
        i=i//2
        st=str(n)+st
    if st==st[::-1]:
        print(temp,"is a palindrome")
    else:
        print(temp,"not a palindrome")
