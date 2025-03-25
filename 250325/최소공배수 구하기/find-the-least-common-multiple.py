n, m = map(int, input().split())

# Please write your code here.
def GCD(n,m):
    n,m=m,n%m
    if m==0 : return n
    else : return GCD(n,m)
    
def LCM(n,m):
    return n*m//GCD(n,m)
    
print(LCM(n,m))