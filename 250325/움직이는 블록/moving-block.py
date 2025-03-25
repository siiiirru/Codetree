n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
blocks_number=sum(blocks)//n
count=0

over_blocks=[x-blocks_number for x in blocks]

for i in range(n):
    while over_blocks[i]<0 :
        max_value=(max(over_blocks))
        max_index=over_blocks.index(max_value)
        over_blocks[max_index]+=over_blocks[i]
        count+=over_blocks[i]*-1
        over_blocks[i]=0

print(count)    