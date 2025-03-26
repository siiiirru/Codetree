arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
a = arr[0]
b = arr[1]
c = arr[3] if a+b == arr[2] else arr[2]

print(a,b,c,sep=" ")