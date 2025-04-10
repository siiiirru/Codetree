n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

def pop():
    #터지기
    for x in range(n): #x축
        same_locate=[]
        same_locate.append((0,x))
        for y in range(1,n): #y축
            if numbers_2d[y][x]==numbers_2d[same_locate[0][0]][same_locate[0][1]] and numbers_2d[y][x] != 0:
                same_locate.append((y,x))
                if y==n-1 and len(same_locate)>=m:
                    for locate in same_locate:
                        numbers_2d[locate[0]][locate[1]]=0
                    same_locate.clear()
            else: 
                if len(same_locate)>=m:
                    for locate in same_locate:
                        numbers_2d[locate[0]][locate[1]]=0
                same_locate.clear()
                same_locate.append((y,x))

def fall():
    for x in range(n):
        #임시 배열
        tmp=[0]*n
        tmp_i=n-1

        #값이 있으면 임시배열 아래에서부터 넣기
        for y in range(n-1,-1,-1):
            if numbers_2d[y][x]>0:
                tmp[tmp_i]= numbers_2d[y][x]
                tmp_i-=1

        #임시 배열을 원래 배열로 복사
        for y in range(n):
            numbers_2d[y][x]=tmp[y]

# 터질 게 없을 때 까지 터트리기
def allpop():
    while True:
            before = [row[:] for row in numbers_2d]  # 이전 상태 저장
            pop()
            fall()
            if numbers_2d == before:  # 변화가 없으면 멈춤
                break

def boom(): 
    if (n==1 and m==1): return 0
    global numbers_2d
    for a in range(k):
        allpop()
        fall()
            
        #회전
        numbers_2d=[list(row) for row in zip(*numbers_2d[::-1])]
        
        fall()
    allpop()
    

    return sum(1 for row in numbers_2d for x in row if x>0)

print(boom())
