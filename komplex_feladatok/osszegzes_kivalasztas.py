import random


def legnagyobb_elem(t):
    max = t[0]
    for x in range(len(t)):
        if t[x] > max:
            max = t[x]
    return max

def legkisebb_elem(t):
    min = t[0]
    for x in range(len(t)):
        if t[x] < min:
            min = t[x]
    return min



def osszegzes_tetele(t):
    osszeg = 0
    for x in t:
        osszeg += x
    return osszeg

def tomb_kiiras(t,c=","):
    for x in range(len(t)):
        if x == len(t) - 1:
            print(t[x])
        else:
            print(t[x],end=c)
        

def tom_feltoltes(szam):
    t=[]
    for x in range(1,szam + 1):
        t.append(random.randint(1,10))
    return t

def bekres():
    szam = -1
    while (szam < 1):
        szam = int(input())
    return szam

def main():
    n = bekres()
    l1 = tom_feltoltes(n)
    tomb_kiiras(l1)
    print(osszegzes_tetele(l1))
    print(legnagyobb_elem(l1))
    print(legkisebb_elem(l1))

main()