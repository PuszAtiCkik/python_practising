
def bevetelvagykiadas(t):
    osszeg = 0
    for x in range(len(t)):
        if t[x] < 0:
            osszeg -= -t[x]
        else:
            osszeg += t[x]
    return osszeg


def main():
    t = [6400, -2000, -4300, 8200, 1000, -3400, 600, -900]
    print(bevetelvagykiadas(t))
main()