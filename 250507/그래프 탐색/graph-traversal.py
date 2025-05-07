n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph=[[0 for _ in range (n+1)]for _ in range (n+1)]
for edge in edges:
    graph[edge[0]][edge[1]]=1
    graph[edge[1]][edge[0]]=1

count=0
visited=[False for _ in range(n+1)]
def dfs(ver):
    global count
    visited[ver]=True
    for curr_v in range(1,n+1):
        if graph[ver][curr_v]==1 and visited[curr_v]==False:
            count+=1
            dfs(curr_v)

    
dfs(1)
print (count)