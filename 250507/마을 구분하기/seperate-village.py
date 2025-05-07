n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
village=[]

di=[(-1,0),(1,0),(0,-1),(0,1)]


def dfs(loc):
    global cnt
    y,x = loc
    if 0<=y<n and 0<=x<n and grid[y][x] ==1:
        grid[y][x] = 2
        cnt+=1
        for dloc in di:
            dy, dx = dloc
            dfs((y+dy,x+dx))

cnt=0
for i in range (n):
    for j in range(n):
        cnt=0
        dfs((i,j))
        if cnt>0:
            village.append(cnt)

village.sort()

print (len(village))
print (*village,sep="\n")