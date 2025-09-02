

def second_largest(arr):
    if len(arr)<2:
        return None
    
    else:
        largest = second = -9999999
        l=[]
        for i in arr:
            if i not in l:
                l.append(i)
        for num in l:
            if num > largest:
                second = largest
                largest = num
            elif num > second:
                second = num
        return second



n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))

print("Second largest:", second_largest(arr))
