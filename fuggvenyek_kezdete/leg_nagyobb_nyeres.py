
def LegnagyobbNyeres(t):
    max = t[0]
    for x in range(len(t)):
        if t[x] > max:
            max = x
    return max - 1


def main():
    t = [6400, -2000, -4300, 8200, 1000, -3400, 600, -900]
    print(LegnagyobbNyeres(t))
main()