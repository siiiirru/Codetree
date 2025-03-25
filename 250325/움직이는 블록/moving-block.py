n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
avg=sum(blocks)//n
count=0

for i in range(n):
    if blocks[i]>avg:
        count+=blocks[i]-avg

print(count)