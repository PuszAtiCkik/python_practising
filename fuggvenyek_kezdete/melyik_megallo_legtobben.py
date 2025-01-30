def Maximum_Kivalasztas(t):
    maxi = t[0]
    megallok = megallokCheckolasa(t)
    for x in range(len(megallok)):
        if megallok[x] > maxi:
            maxi = x
    return maxi


def megallokCheckolasa(t):
    megallok = []
    for x in range(0, len(t), 2):  
        megallok.append(t[x])
    return megallok


def main():
    t = [2, 0, 4, 1, 15, 11, 100, 14, 16, 2, 0, 109]
    print(Maximum_Kivalasztas(t))  

main()
