n, m, r, c = map(int, input().split())

# Please write your code here.
dir=[(-1,0),(0, 1), (1,0),(0,-1)]
grid = [[0 for _ in range (n)] for _ in range(n)]
grid[r-1][c-1]=1


# 놓여져 있는 전체 폭탄 위치 리스트
boom_list=[]
boom_list.append((r-1,c-1))


def print_grid():
    for i in grid:
        print(*i)
    print("---")


def lets_boom ():
    for time in range (1,m+1):
        boom_count=len(boom_list)
        for i in range (boom_count):
            for d in dir:
                dy=boom_list[i][0]+d[0]*(2**(time-1))
                dx=boom_list[i][1]+d[1]*(2**(time-1))
                if dy>=0 and dy <n and dx>=0 and dx<n and grid[dy][dx]==0:
                    grid[dy][dx]=1
                    boom_list.append((dy,dx))
        # print(time)
        # print_grid()
                    

                    

lets_boom()
print(len(boom_list))


            
            
