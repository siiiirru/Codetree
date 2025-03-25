n = int(input())
sequence = list(map(int, input().split()))
sorted_sequence= sorted(sequence)

first_min= True
count= 0
# Please write your code here.
for i in range (n):
    if sequence == sorted_sequence: 
        break

    min_val=min(sequence)
    max_val=max(sequence)

    if sequence[0] == min_val:
        if first_min == True:
            max_index= sequence.index(max_val)
            sequence.pop(0)
            sequence.insert(max_index,min_val)
            count+=1
    elif sequence[0] == max_val:
        sequence.pop(0)
        sequence.append(max_val)
        count+=1
    else: 
        min_index=sequence.index(min_val)
        max_index=sequence.index(max_val)
        for j in range(min(n,max_index+1),n):
            if sequence[0]>sequence[j] or j==n:
                val=sequence.pop(0)
                sequence.insert(j,val)
                count+=1
                break

print (count)