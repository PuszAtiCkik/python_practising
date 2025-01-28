import random

def elofordulas_szamolasa(t, elem):
    count = 0
    for i in range(len(t)):
        if t[i] == elem:
            count += 1
    return count

def legtobb_elofordulas(t):
    max_count = 0
    max_elements = []
    for i in range(len(t)):
        count = elofordulas_szamolasa(t, t[i])
        if count > max_count:
            max_count = count
            max_elements = [t[i]]
        elif count == max_count and t[i] not in max_elements:
            max_elements.append(t[i])
    return max_count, max_elements

def lista_letrehozas(szam):
    t = [random.randint(1, 6) for _ in range(szam)]
    return t

def bekeres():
    szam = -1
    while szam <= 1:
        szam = int(input("Add meg a lista hosszát (legalább 2): "))
    return szam

def main():
    n = bekeres()
    l1 = lista_letrehozas(n)
    print("Generált lista:", l1)
    max_count, max_elements = legtobb_elofordulas(l1)
    print(f"A legtöbbször előforduló szám(ok): {max_elements}, előfordulások száma: {max_count}")

if __name__ == "__main__":
    main()
