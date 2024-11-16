a = input()
x = 0
y = 0
c = 0
for i in a:
    if i == "R":
        x += 1
    if i == "L":
        x -= 1
    if i == "U":
        y += 1
    if i == "D":
        y -= 1
    if x == 0 and y == 0:
        c += 1
print(c)
