N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
i=0
even=0
odd=0
result=0
for i in range(N):
    if numbers[i]%2==0:
        even+=1
    else :
        odd+=1

if 0<=(even - odd)<2:
    result=N
else:
    diff=abs(odd-even)
    # 홀, 짝 중 하나의 갯수가 0이 아닌 경우
    if diff!=N: 
        result=min(odd,even)*2
        if diff%2==0: result+=diff//2
        else : result+=diff//2+1
    elif odd==N: result=N//2
    else : result=1 
    
print (result)