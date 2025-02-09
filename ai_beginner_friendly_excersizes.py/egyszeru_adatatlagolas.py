

def atlagolas(t):
    osszeg = osszegzes(t)
    return osszeg / len(t)
def osszegzes(t):
    tomb = listahoz_adas_szamokat(t)
    osszeg = 0
    for x in tomb:
        osszeg += x
    return osszeg

def listahoz_adas_szamokat(inp):
    szamok = [int(x) for x in inp]
    return szamok


def main():
    user_inp = input().split(" ")
    # print(osszegzes(user_inp))
    print(atlagolas(user_inp))


main()