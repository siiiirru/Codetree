n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
mid_index=len(arr)//2

result=float('inf')
for i in range(mid_index):
   if result > arr[mid_index+i]-arr[i]:
    result = arr[mid_index+i]-arr[i]

print(result)