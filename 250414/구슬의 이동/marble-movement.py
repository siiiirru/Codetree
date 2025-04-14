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

class Marbles :

    def __init__(self):
        # 이동하는 구슬의 위치 딕셔너리. key는 위치, value는 구슬 인덱스
        self.marbles={}
        # 0초에서 구슬의 위치 초기화
        for i in range (m):
            self.marbles[(r[i],c[i])]=[i]

    def move(self,i):
        if a[i]==True: 
            #이전 위치는 위치 딕셔너리에서 지우기
            if len(self.marbles[(r[i],c[i])])>1:
                self.marbles[(r[i],c[i])].remove(i)
            else: del self.marbles[(r[i],c[i])]
            # 각 구슬들의 속도만큼 한칸씩 이동하며 벽에 부딪히는지 검사
            for block in range (v[i]):
                dy=r[i]+dir[d[i]][0]
                dx=c[i]+dir[d[i]][1]
                # 벽에 부딪혔을 때는 방향 바꿔서 이동
                if dy<0 or dy>=n or dx<0 or dx>=n :
                    d[i]=self.change_dir(d[i])
                    dy=r[i]+dir[d[i]][0]
                    dx=c[i]+dir[d[i]][1]
                r[i]=dy
                c[i]=dx

            # 이동한 곳으로 위치 딕셔너리 업데이트
            if (r[i],c[i]) in self.marbles:
                self.marbles[(r[i],c[i])].append(i)
            else: self.marbles[(r[i],c[i])]=[i]

    # 방향 전환
    def change_dir(self,original_d):
        direction_map = {
            "L": "R",
            "R": "L",
            "U": "D",
            "D": "U"
        }
        return direction_map.get(original_d)

    # 같은 위치에 k이상의 구슬이 있을 경우 삭제
    def remove_same_locate(self):
        for key in list(self.marbles.keys()):
            while len(self.marbles[key]) > k:
                # 속도가 낮은 값부터 삭제
                value = self.marbles[key]
                vlist = [v[i] for i in value]
                min_val = min(vlist)
                # 낮은 값이 여러개면 인덱스가 작은 값부터 삭제
                min_val_index = [i for i in value if v[i] == min_val and a[i]]
                min_index = min(min_val_index)
                a[min_index] = False
                self.marbles[key].remove(min_index)
                # 같은 위치 구슬 개수 다시 갱신
                # (이걸로 while 조건에도 바로 반영됨)

def move_marbles():
    marbles=Marbles()
    for time in range(t):
        for i in range (m):
            marbles.move(i)
        marbles.remove_same_locate()

move_marbles()
result=0
for i in a:
    if i==True:
        result+=1

print(result) 


                            
