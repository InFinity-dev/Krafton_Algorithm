a = input()
b = input()

# b의 1의자리 수
c = int(b[2])
# b의 10의자리 수
d = int(b[1])
# b의 100의자리 수
e = int(b[0])

print(int(a) * c)
print(int(a) * d)
print(int(a) * e)
print(int(a) * int(b))
