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
    if even>odd:
        result=odd*2+1
    else :
        result=even*2
        diff=odd-even
        if diff%2==0:
            result+=diff//2+1
        elif (diff//2)%2==0: result+=diff//2+1
        else : result+=diff//2

print (result)