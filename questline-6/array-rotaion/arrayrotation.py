n = int(input("Enter how many numbers: "))
arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter number: "))
l = len(arr)
rotated = arr[-k:] + arr[:-k]
print(rotated)
             
    

