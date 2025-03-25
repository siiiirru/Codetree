n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt=0
i=0
while i<n:
    if arr[i]==0: 
        i+=1 
        continue
    for j in range (i,i+m*2):
        if arr[j]==1: 
            cnt+=1
            i+=m*2+1
            break

print(cnt)