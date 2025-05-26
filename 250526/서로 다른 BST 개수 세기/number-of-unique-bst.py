n = int(input())

dp=[1]*(n+1)
# Please write your code here.

#즉, 루트를 k로 고정하면,
#왼쪽 서브트리로 만들 수 있는 BST의 개수 × 오른쪽 서브트리로 만들 수 있는 BST의 개수가
#루트를 k로 할 때 만들 수 있는 BST 개수가 되는 거야.
#DP[0] = 1 (노드가 없을 때도 하나의 BST로 본다)
#DP[1] = 1
# dp[2]=dp[1]*2
# dp[3]=dp[2]*2+dp[1]
# dp[4]=dp[3]*2+(dp[1]*dp[3])+(dp[2]*dp[1])
# dp[i]=(dp[i-1]*2)+dp[0]*dp[i-1]+dp[1]*dp[i-2]

for i in range (1, n+1):
    if i<=2:
        dp[i]=i
    elif i==3:
        dp[i]=5
    else :
        sum=dp[i-1]*2
        for j in range(i//2):
            sum+=dp[j]*dp[i-(j+1)]
        dp[i]=sum

print (dp[n])
