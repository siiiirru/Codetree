from collections import deque
n = int(input())
sequence = deque(list(map(int, input().split())))
sorted_sequence = deque(sorted(sequence))
count = 0
min_val = min(sequence)
max_val = max(sequence)
min_first = True
# Please write your code here.
if sequence != sorted_sequence:
    for i in range (n): 
        val=sequence.popleft()
        if val == max_val:
            sequence.append(val)
            count += 1
        elif val == min_val:
            if min_first == False : 
                break
            else : 
                min_first = False
            past_tail = sequence[-1]
            if past_tail == max_val:
                past_tail = sequence[-2]
            for j in range(n-3,-1,-1):
                if past_tail < sequence[j]:
                    sequence.insert(j+1,val)
                    count+=1
                    break
        else :
            past_tail = sequence[-1]
            if past_tail == max_val:
                past_tail = sequence[-2]
            for j in range(n-3,-1,-1):
                if past_tail < sequence[j]:
                    start = j
                    new_sequence = [val-x for x in sequence]
                    new_sequence_positive = list(map(lambda x : 100 if x<0 else x, new_sequence))
                    new_sequence_positive[0:j]= [100] * (j)
                    insert_index = new_sequence_positive.index(min(new_sequence_positive))
                    sequence.insert(insert_index+1,val)
                    count+=1
                    break
                if past_tail < val and val != max_val:
                    sequence.insert(-1,val)
                    count+=1
                    break
            

print (count)