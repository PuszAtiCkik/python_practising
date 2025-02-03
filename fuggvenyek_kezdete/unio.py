def unio(t1,t2):
    unio = t1
    for elem in t2:
        benne_van = False
        for x in unio:
            if x == elem:
                benne_van = True
        if benne_van:
            unio.append(elem)
    return unio



def main():
    t1 = [1, 3, 5, 7, 9, 11]
    t2 = [3, 4, 7, 8, 10, 11]
    print(unio(t1,t2))
main()