n = int(input())

def print_square(N):
    i=1
    for _ in range(N):
        for _ in range(N):
            if i>9: i=1
            print(i,end=" ")
            i+=1
        print()

print_square(n)
# Please write your code here.