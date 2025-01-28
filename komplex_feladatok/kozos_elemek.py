def kozos_elemek(t1,t2):
    elemek = []
    for elem in t1:
        if elem in t2 and elem not in elemek:
            elemek.append(elem)
    return elemek
        


def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = [3, 4, 5, 6, 7]
    print(kozos_elemek(l1,l2))
main()