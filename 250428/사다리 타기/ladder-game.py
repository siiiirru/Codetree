n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
# Please write your code here.

# def print_hline(line,b):
#     b=0
#    a or a-1 이 i인 것중 b가 높은 것으로 옮겨가기
#     그 줄에 더이상 a or a-1가 없을 때 까지 옮겨간 것 


#주어진 사다리의 도착지 배열 만들기
def match(edges):
    match_arr=[x for x in range (n)]
    if len(edges)==0:
        return match_arr
    new_edges = sorted(edges, key=lambda x: x[1])
    for i in range (n): 
        line=i
        b=0
        for index in range(len(edges)):
            if new_edges[index][1] > b: #배열 범위 넘어감
                if new_edges[index][0]==line+1 :
                    line=new_edges[index][0];
                    b=new_edges[index][1]
                    continue
                elif new_edges[index][0]+1==line+1:
                    line=new_edges[index][0]-1
                    b=new_edges[index][1]
                    continue
        #i번째 줄의 최종 도착지를 배열에 저장
        match_arr[i]=line
    return match_arr

min_line=m
#사다리 한줄씩 그리기
def draw_min_line(edges,line_count):
    global min_line
    if line_count>=min_line:
        return 
    # 최종매치되면 최소사다리선 개수 업데이트
    if match(edges)==first_match_arr:
        min_line=min(min_line,line_count)
        return 
    
    # 라인 그리기
    for i in range (n-1):
        edges.append((i+1,line_count+1))
        draw_min_line(edges,line_count+1)
        if len(edges)>0:
            edges.pop()

    return


first_match_arr=match(edges)
new_edges=list()
draw_min_line(new_edges,0)
print(min_line)