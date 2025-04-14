n, m, t, k = map(int, input().split())
# a는 활성화된 인덱스를 표시하기 위함
r, c, d, v, a = [], [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri)-1)
    c.append(int(ci)-1)
    d.append(di)
    v.append(int(vi))
    a.append(True)

# Please write your code here.
# 방향
dir = {"L" : (0,-1), "U" : (-1,0), "R" : (0,1), "D" : (1,0)}

# 이동하는 구슬의 위치 딕셔너리
marbles={}


# 0초에서 구슬의 위치
for i in range (m):
    marbles[(r[i],c[i])]=[i]

def change_dir(original_d):
    direction_map = {
        "L": "R",
        "R": "L",
        "U": "D",
        "D": "U"
    }
    return direction_map.get(original_d)


# 시간의 흐름. 1초부터 시작
def move_marbles():
    for time in range(t):
        # 구슬들의 이동
        for i in range (m):
            # 활성화 된 구슬만 이동
            if a[i]==True: 
                #이전 위치는 지우기
                if len(marbles[(r[i],c[i])])>1:
                    marbles[(r[i],c[i])].remove(i)
                else: del marbles[(r[i],c[i])]
                # 각 구슬들의 속도만큼 한칸씩 이동하며 벽에 부딪히는지 검사
                for block in range (v[i]):
                    dy=r[i]+dir[d[i]][0]
                    dx=c[i]+dir[d[i]][1]
                    # 벽에 부딪혔을 때는 방향 바꿔서 이동
                    if dy<0 or dy>=n or dx<0 or dx>=n :
                        d[i]=change_dir(d[i])
                        dy=r[i]+dir[d[i]][0]
                        dx=c[i]+dir[d[i]][1]
                    r[i]=dy
                    c[i]=dx

                #새로 위치 업데이트
                if (r[i],c[i]) in marbles:
                    marbles[(r[i],c[i])].append(i)
                else: marbles[(r[i],c[i])]=[i]

        # 충돌 시 사라짐
        for value in marbles.values():
            while len(value)>k:
                # 속도가 작은 것 부터 비활성화
                vlist = [v[i] for i in value]
                min_val=min(vlist)
                min_val_index=[ind for ind,val in enumerate(v) if val==min_val and a[ind] is True]
                min_index=0
                # 작은 값이 여러개면 인덱스 값이 낮은 값을 비활성화
                if len(min_val_index)>1:
                    min_index=min(min_val_index)
                else :
                    min_index=min_val_index[0]
                a[min_index]=False
                # 위치 지우기
                marbles[(r[min_index],c[min_index])].remove(min_index)


move_marbles()
result=0
for i in a:
    if i==True:
        result+=1

print(result) 


                            
