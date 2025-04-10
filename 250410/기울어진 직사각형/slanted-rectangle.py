n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_result=0

# 제일 위의 꼭지점이 이동함. 아래로만 영역 확장
# y축으로 이동 가능한 범위
for y in range(n-2):
    #x축으로 이동 가능한 범위
    for x in range(1,n-1):
        # 제일 작은 범위 다이아몬드 합산
        top = grid[y][x]
        left = grid[y+1][x-1]
        right = grid[y+1][x+1]
        bottom = grid[y+2][x]
        diamond = top+left+right+bottom
        if diamond > max_result:
            max_result = diamond

        # y축 아래로 확장이 가능하다면
        if y<n-3:
            # py는 확장 블록 중 제일 위의 y위치, pxl은 왼쪽 확장 블록 제일 위의 x위치, pxr은 오른쪽 확장 블록 제일 위의 x위치
            py = y+2
            pxl = x-2
            pxr = x+2
            prsum = diamond
            plsum = diamond
            while py < n-1 :
                #왼쪽 아래 확장
                if pxl >= 0:
                    plsum += grid[py][pxl] + grid[py+1][pxl+1]
                    if plsum > max_result :
                        max_result = plsum
                    pxl-=1
                
                #오른쪽 아래 확장
                if pxr < n :
                    prsum += grid[py][pxr] + grid[py+1][pxr-1]
                    if prsum > max_result :
                        max_result = prsum
                    pxr+=1

                py+=1

print(max_result)


            
