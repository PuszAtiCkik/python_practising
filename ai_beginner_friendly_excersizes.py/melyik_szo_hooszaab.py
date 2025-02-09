
def hosszabb(t):
    maxx = t[0]
    for x in t:
        if len(x) > len(maxx):
            maxx = x
    return maxx

       

szavak = []
adat = input().split(",")
for s in adat:
    szavak.append(s)

print(hosszabb(szavak))