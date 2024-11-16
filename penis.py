n = int(input())
b = []
f = []
for i in range(n):
    b.append(input())
s = input()
for i in b:
    if i[-1] == s[-1]:
        f.append(i)
print(f)
