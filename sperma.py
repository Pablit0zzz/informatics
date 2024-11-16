n = int(input())
s = 0
c = 0
for i in range(n):
    num = float(input())
    if num < 0:
        c += 1
        s += num
print(s/c)
