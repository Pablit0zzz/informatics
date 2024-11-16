a = int(input())
b = 0
c = 0
for i in range(a):
    v = float(input())
    if v < 0:
        b += v
        c += 1
if c == 0:
    print(0)
else:
    print(b/c)
