n = int(input())
blocks = list(map(int, input().split()))
count = 0
for i in range(n-1,-1,-1):
    if i-1>0 and blocks[i-1]>blocks[i] :
        count = i
            

print (count)