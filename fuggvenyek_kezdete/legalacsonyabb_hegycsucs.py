
def legkissebbHegycsucs(t):
    min = t[1]
    for x in range(len(t) -1):
        if t[x -1] > t[x] < t[x + 1]:
            if t[x - 1] < min:
                min = t[x-1]
    return min

def main():
    t = [0, 500, 100, 700, 350, 650, 20, 550, 10, 0]
    print(legkissebbHegycsucs(t))
main()