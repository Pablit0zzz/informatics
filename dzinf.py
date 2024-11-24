n = int(input())
m = 999999
for i in range(n):
    a = int(input())
    if 1344 % a == 0 and m > a: m = a
print(m)

a = int(input())
s = 0
while a != 0:
    if a % 7 == 0 and a % 10 == 2: s += a
    a = int(input())
print(s)
