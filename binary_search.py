a = [0, 2, 5, 7, 9, 899, 1000, 12498071249087]

t = int(input())

def search(t):
    mi = 0
    ma = len(a)-1
    while mi <= ma:
        if t > a[(mi+ma)//2]: mi = (mi+ma)//2+1
        elif t < a[(mi+ma)//2]: ma = (mi+ma)//2-1
        else: return (mi+ma)//2
    return -1

print(search(t))
