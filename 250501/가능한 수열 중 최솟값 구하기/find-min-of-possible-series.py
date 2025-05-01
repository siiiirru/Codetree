n = int(input())

# Please write your code here.
arr=[]
ans=[6 for _ in range(n)]
def possible_print(cnt):
    global ans
    #길이 다 채우면 최소 수열 갱신
    if cnt ==n: 
        # print("끝. 만들어진 수열:",arr,"비교할 최소 수열:",ans)
        sort_arr=[arr[:],ans]
        sort_arr.sort()
        ans=sort_arr[0]
        # print("갱신된 수열:",ans)
        return

    for i in range (4,7):
        is_possible=True
        # 불가능 수열 걸러내기
        arr.append(i)
        if cnt==1 and arr[0]==arr[1]:
            arr.pop()
            is_possible=False
        for j in range(0,(cnt+1)//2):
            #비교 대상의 개수가 충분할 때
            if (cnt+1)//2>j:
                if arr[cnt-(j*2)-1:cnt-j]==arr[cnt-j:cnt+1]:

                    arr.pop()
                    is_possible=False
                    break

        if is_possible is False: continue
                
        possible_print(cnt+1)
        arr.pop()


possible_print(0)
print(*ans, sep='')