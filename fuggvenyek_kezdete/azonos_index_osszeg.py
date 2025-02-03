def index_sum(t1,t2):
    osszegek = []
    for x in range(len(t1)):
        osszeg = t1[x] + t2[x]
        osszegek.append(osszeg)
    return osszegek

def main():
    t1 = [1, 2, 3, 4, 5]
    t2 = [10, 20, 30, 40, 50]
    print(index_sum(t1,t2))
main()