
def primszam_ellenorzes(szam):
    if szam < 2:
        return False
    for oszto in range(2,int(szam**0.5) + 1):
        if szam % oszto == 0:
            return False
    return szam


def intervallum(kezd,vege):
    primszamok = []
    for x in range(kezd,vege):
        if primszam_ellenorzes(x):
            primszamok.append(x)
    return primszamok



def main():
    kezdes = 10
    vege = 50
    print(intervallum(kezdes,vege))
main()