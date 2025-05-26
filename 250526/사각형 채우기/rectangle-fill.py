n = int(input())

# Please write your code here.
dp=[0]*(n+1)

for i in range(1,n+1):
    if i<=2:dp[i]=i
    else : dp[i]=dp[i-1]+dp[i-2]

result=dp[n]%10007
print(result)