x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
c1 = min(x1,a1)
d1 = min(y1,b1)
c2 = max(x2,a2)
d2 = max(y2,b2)
result = (c2-c1)*(d2-d1)
print(result)