a = int(input())
b = []
c = []
for i in range(a):
    b.append(input())
v = input()
for i in b:
    if i[-1] == v[-1]:
        c.append(i)
print(c)
