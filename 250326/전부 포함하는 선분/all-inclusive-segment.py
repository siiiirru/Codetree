n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x1_sorted_segments = sorted(segments,key = lambda x: x[:][0])
x2_sorted_segments = sorted(segments,key = lambda x: x[:][1])

x1_diff = x1_sorted_segments[1][0]-x1_sorted_segments[0][0]
x2_diff = x2_sorted_segments[-1][1]-x2_sorted_segments[-2][1]

result = 0
if x1_diff >= x2_diff:
    result = x2_sorted_segments[-1][1]-x1_sorted_segments[1][0]
else :
    result = x2_sorted_segments[-2][1]-x1_sorted_segments[0][0]

print (result)