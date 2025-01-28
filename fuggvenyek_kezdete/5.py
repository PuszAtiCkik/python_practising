def karakter_szamolas(karakter):
    osszeg = 0
    for x in karakter:
        osszeg += 1
    return osszeg

def main():
    szoveg = input()
    print(karakter_szamolas(szoveg))

main()