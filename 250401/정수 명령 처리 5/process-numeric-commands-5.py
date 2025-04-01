N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

arr = []
# Please write your code here.
for i in range(N):
    match command[i]:
        case "push_back":
            arr.append(num[i])
        case "get":
            print(arr[num[i]-1])
        case "size":
            print(len(arr))
        case "pop_back":
            arr.pop()
        case _:
            print()
            