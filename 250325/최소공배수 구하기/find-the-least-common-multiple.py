n, m = map(int, input().split())

# Please write your code here.
def GCD(n,m):
    while m>0:
        n,m=m,n%m
    return n

def LCM(n,m):
    return int(n*m/GCD(n,m))
    
print(LCM(n,m))