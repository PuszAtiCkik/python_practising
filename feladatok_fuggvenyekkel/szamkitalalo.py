import random

# A számítógép által generált véletlen szám
def gep_szama():
    return random.randint(1, 100)

# Tipp ellenőrzése
def tipp_ellenorzese():
    tippek = int(input("Adj meg egy tippet (1 és 100 között): "))
    while tippek < 1 or tippek > 100:  # Tipp validálása
        tippek = int(input("Helytelen szám! Adj meg egy tippet 1 és 100 között: "))
    return tippek

# Tippelés visszajelzése
def tipp_visszajelzes(tipped, gep_szama):
    if tipped > gep_szama:
        print("Fölé ment!")
    elif tipped < gep_szama:
        print("Alá ment!")
    else:
        print("Gecijó vagy, eltaláltad!")

# A fő függvény, ami összerakja a játékot
def main():
    print("Számkitaláló játék")
    gep_tippe = gep_szama()  # Generáljuk a számítógép számát
    eltalaltad = False

    # Addig folytatódik a játék, amíg el nem találja a számot
    while not eltalaltad:
        tipp = tipp_ellenorzese()  # Tippel a játékos
        if tipp == gep_tippe:  # Ellenőrizzük, hogy eltalálta-e
            print("Gecijó vagy, eltaláltad!")
            eltalaltad = True
        else:
            tipp_visszajelzes(tipp, gep_tippe)  # Adj visszajelzést a tipphez

# A játék indítása
main()
