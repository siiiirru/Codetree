arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
a = arr[0]
b = arr[1]
c = arr[2]
d = arr[-1]-a-b-c
print(a, b, c, d)