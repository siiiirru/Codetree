n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr_sorted=sorted(arr)
mid_index=len(arr_sorted)//2
diff_arr=[]

for i in range(mid_index):
    diff_arr.append(arr_sorted[mid_index+i]-arr_sorted[i])

result = min(diff_arr)
print(result)