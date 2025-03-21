n = int(input())

def print_square(N):
    i=0
    for _ in range(N):
        for _ in range(N):
            print(i%9+1,end=" ")
            i+=1
        print()

print_square(n)
# Please write your code here.