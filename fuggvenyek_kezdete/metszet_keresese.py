
def metszet_meghatarozasa(t1,t2):
    metszet = []
    for x in range(len(t1)):
        for y in range(len(t2)):
            if t1[x] == t2[y]:
                metszet.append(t2[y])
    return metszet


def main():
    t1 = [1, 3, 5, 7, 9, 11, 13]
    t2 = [2, 3, 6, 7, 10, 13, 15]
    print(metszet_meghatarozasa(t1,t2))
main()