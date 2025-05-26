n = int(input())

# Please write your code here.

dp=[0]*(n+1)

dp[0]=0
dp[1]=0

for i in range(2,n+1):
    if i==2 or i ==3: dp[i]=1
    else : dp[i]=dp[i-2]+dp[i-3]

result=dp[n]%10007
print(result)