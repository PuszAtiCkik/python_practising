import math

def osszegzes(t):
    osszeg = 0
    for x in t:
        osszeg += x
    return osszeg

def atlagszamitas(t):
    return osszegzes(t) / len(t)

def eltérés_szamolasa(t):
    atlag = atlagszamitas(t)
    return [(x - atlag) ** 2 for x in t]

def szoras(t):
    adat = eltérés_szamolasa(t)
    return math.sqrt(osszegzes(adat) / len(t))

def kozepso_elemek(t):
    n = len(t)
    if n % 2 == 1:
        return [t[n // 2]]
    else:
        return [t[n // 2 - 1], t[n // 2]]

def kozepsoSzamok_osszege(t):
    return osszegzes(kozepso_elemek(t))

def tombrendezés(tomb):
    for x in range(len(tomb) - 1):
        for y in range(len(tomb) - x - 1):
            if tomb[y] > tomb[y + 1]:
                tomb[y], tomb[y + 1] = tomb[y + 1], tomb[y]
    return tomb

def median(t):
    rendezett_t = tombrendezés(t.copy())  # Sort a copy to avoid modifying the original list
    return kozepsoSzamok_osszege(rendezett_t) / len(kozepso_elemek(rendezett_t))

def main():
    t = [60, 75, 80, 90, 85, 70, 95, 10]

    print("Átlag:", atlagszamitas(t))
    print("Medián:", median(t))
    print("Szórás:", round(szoras(t), 2))

main()
