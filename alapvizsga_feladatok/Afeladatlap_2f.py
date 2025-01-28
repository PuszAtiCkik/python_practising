szam1 = 25
szam2 = 33
counter = 0

for x in range(szam1,szam2 + 1):
    if x == szam2 :
        print(x,end=" ")
    else:
        print(x,end=", ")
    if x % 3== 0:
        counter +=1

print(counter)

