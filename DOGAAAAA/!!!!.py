import random



def kiiras(t):
    counter = LegkisebbElemekSZamlalasa(t)
    min_szam = LegkisebbSZamMegtalalas(t)
    print(f"a legkisebb szam {min_szam} abbol {counter} db van")



def LegkisebbElemekSZamlalasa(t):
    counter = 0
    min_szam = LegkisebbSZamMegtalalas(t)
    for x in range(len(t)):
        if t[x] == min_szam:
            counter += 1
    return counter




def LegkisebbSZamMegtalalas(t):
    min = t[0]
    for x in range(len(t)):
        if t[x] < min:
            min = t[x]
    return min

def tomb_kiiras(tomb, operator="\n"):
    for x in range(len(tomb)):
        if (x + 1) % 10 != 0:
            print(tomb[x], end=" ")
        else:
            print(tomb[x],end=operator)

def tomb_feltoltes(szam):
    t = []
    for x in range(szam):
        t.append(random.randint(1,20))
    return t



def bekeres():
    szam = -1
    while szam <= 1:
        szam = int(input(" "))
    return szam


def main():
    n = bekeres()
    t1 = tomb_feltoltes(n)
    tomb_kiiras(t1)
    print()
    kiiras(t1)
main()