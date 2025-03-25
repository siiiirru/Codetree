n, m = map(int, input().split())

# Please write your code here.
def GCD(n,m):
    r=n%m
    if r==0 :return m
    else: return GCD(m,r)

print(GCD(n,m))