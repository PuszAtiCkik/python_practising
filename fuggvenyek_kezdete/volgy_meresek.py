


def volgy_kereses(t):
    max = t[0]
    for x in range(len(t)-1):
        if t[x - 1 ] > t[x] < t[x + 1]:
            if t[x] > max:
                max = x - 1
    return max
        

def main():
    t = [0, 500, 100, 700, 350, 650, 20, 550, 10, 0]
    print(volgy_kereses(t))
main()