import random



def listához_adás(szam):
    t=[]
    for x in range(1,szam + 1):
        t.append(random.randint(1,100))
    return t

def bekeres():
    szam = int(input())
    while (szam < 1):
        szam = int(input())
    return szam

def osszefuttatas_algoritmus(l1,l2):
    results = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            results.append(l1[i])
            i += 1
        else:
            results.append(l2[j])
            j+=1
    while i < len(l1):
        results.append(l1[i])
        i+=1
    while j < len(l2):
        results.append(l2[j])
        j+=1
    return results

def buborékos_rendezés(lista):
    n = len(lista)
    for x in range(n):
        for j in range(0, n - x - 1):
            if lista[j] >lista[j + 1]:
                lista[j],lista[j + 1] = lista[j + 1],lista[j]
    return lista


def main():
    l1 = bekeres()
    l2 = bekeres()
    t1 = listához_adás(l1)
    t2 = listához_adás(l2)
    print(t1)
    print(t2)
    tt1 = buborékos_rendezés(t1)
    tt2 = buborékos_rendezés(t2)
    print(osszefuttatas_algoritmus(tt1,tt2))

main()