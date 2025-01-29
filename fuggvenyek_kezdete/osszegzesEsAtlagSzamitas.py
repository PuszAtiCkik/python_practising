
def AtlagSzamitas(t):
    osszeg = osszegzes(t)

    atlag = osszeg / len(t)
    return atlag


def osszegzes(t):
    osszeg = 0
    for x in range(len(t)):
        osszeg += t[x]
    return osszeg


def main():
    t = [4, 6, 8, 2, 10]
    print(osszegzes(t))
    print(AtlagSzamitas(t))


main()