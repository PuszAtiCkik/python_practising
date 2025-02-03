

def kiiras(t,char=", "):
    for x in range(len(t)):
        if x == len(t) - 1:
            print(t[x],end="")
        else:
            print(t[x],end=char)

def Megrging2lists(t1,t2):
    alap_lista = t1
    for x in range(len(t2)):
        alap_lista.append(t2[x])
    return alap_lista

def main():
    t1 = [1, 2, 3, 4]
    t2 = [5, 6, 7, 8]
    alap = Megrging2lists(t1,t2)
    kiiras(alap)
main()