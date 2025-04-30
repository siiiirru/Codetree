n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

ans=0
# Please write your code here.

# 물건 선택 후 가치 반환 
def get_value(items):
    value=0
    items_sum=0
    for idx,item in enumerate (items):
        items_sum+=item
        if(items_sum)>c:
            break
        value+=item**2
    return value

# 최대가치 갱신하기
def update_max(a,b):
    global ans
    value_sum=0
    a_items=weight[a[0]][a[1]:a[1]+m]
    b_items=weight[b[0]][b[1]:b[1]+m]
    a_items.sort(reverse=True)
    b_items.sort(reverse=True)
    value_sum+=get_value(a_items)
    value_sum+=get_value(b_items)
    ans=max(value_sum,ans)
    return 

#자리 옆으로 한칸씩 옮기기
def move(loc):
    new_loc = list(loc)
    if new_loc[1] >= n - m:
        new_loc[0] += 1
        new_loc[1] = 0
    else:
        new_loc[1] += 1
    if new_loc[0] >= n or new_loc[1]>n-m: return None
    return tuple(new_loc)

finish=False
def go (a,b):
    global finish
    #B가 끝에 왔으면 return
    if b is None or a is None :
        return

    update_max(a,b)

    #A는 두고 B만 움직임
    b=move(b)
    go(a,b)

    if not finish:
        #A전진 B는 A다음 위치에
        a=move(a)
        if a is not None:
            b = move((a[0], a[1] + m - 1))
            if b is not None:
                go(a, b)
            #A 다음 B가 끝에 도달하면 종료
            else: finish=True

go((0,0),move((0,0+m)))
print(ans)