x, y = map(str, input().split())
x_rev, y_rev = x[::-1], y[::-1]
compare = []
compare.extend([x_rev, y_rev])
print(max(compare))
