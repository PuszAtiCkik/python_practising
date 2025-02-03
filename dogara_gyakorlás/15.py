

def masodikFeladat(t):
    i = 0
    keresett_szam = int(input())
    while i < len(t) and not t[i] > keresett_szam:
        i+= 1
    if i < len(t):
        print(f"igen volt {i}")
    else:
        print("nem")


def elso_feladatKiiras(t):
    perc,remainder = masodperc_percre_masodpercre(t)
    print(f"{perc} p és {remainder} s")

def masodperc_percre_masodpercre(t):
    masodperc = masodperc_szamolas(t)
    perc = masodperc // 60
    remainder = masodperc % 60
    return perc,remainder

def masodperc_szamolas(t):
    masodperc = 0
    for x in range(len(t)):
        masodperc += t[x]
    return masodperc

def main():
    t = [100, 110, 200, 150, 300, 180, 150, 150, 100, 100]
    elso_feladatKiiras(t)
    masodikFeladat(t)

main()