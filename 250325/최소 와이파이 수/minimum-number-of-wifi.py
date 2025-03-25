n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt=0
for i in range(0,n,m*2):
    if arr[i]==0:
        continue
    for j in range (i,i+m*2):
        if arr[j]==1: 
            cnt+=1
            break

print(cnt)