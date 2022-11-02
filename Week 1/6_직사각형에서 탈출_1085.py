x, y, w, h = map(int, input().split())
a = w - x
b = h - y
if a >= x:
    a = x
if b >= y:
    b = y
if a > b:
    print(b)
else:
    print(a)
