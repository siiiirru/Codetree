n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt=0
i=0
while i<n:
    if arr[i]==0: 
        i+=1 
        continue
    else :
        cnt+=1
        i+=m*2+1

print(cnt)