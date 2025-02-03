import random


# def ElsoFeladatKiirasa():


def negyedikfkiiras(t):
    i_index = negyedikF(t)
    if i_index <len(t):
        print("van benne")
    else:
        print("nincs bene")

def negyedikF(t):
    i = 0
    while i <len(t) and t[i] != 0:
        i+= 1
    return i
        

def harmadiFKiirasa(t):
    max_db, max_ertek = harmadik_feladat(t)
    print(f"A {max_ertek} pont fordult elő benne legtöbbször ({max_db} alkalommal)")

def harmadik_feladat(t):
    max_ertek = t[0]
    max_db = 0
    for i in range(len(t)):
        db = 0
        for j in range(len(t)):
            if t[i] == t[j]:
                db += 1
        if db > max_db:
            max_db = db
            max_ertek = t[i]
    return max_db, max_ertek

def Maosik_feladat(t):
    if otosok(t) > eggyesek(t):
        print("tobb otos mint eggyes")
    else:
        print("tobb eggyes mint otos")

def elsoFKiirasa(t):
    harmas = harmasok(t)
    return round((harmas / len(t)) * 100,2)



def eggyesek(t):
    eggyesek = 0
    for score in t:
        percentage = (score / 40) * 100
        if percentage > 0 and percentage < 29:
            eggyesek += 1
    return eggyesek


def harmasok(t):
    harmas = 0
    for score in t:
        percentage = (score / 40) * 100
        if percentage > 50 and percentage < 69:
            harmas += 1
    return harmas


def otosok(t):
    otos = 0
    for score in t:
        percentage = (score / 40) * 100
        if percentage > 85 and percentage < 100:
            otos += 1
    return otos


def tombfeltoltes(szam):
    t = []
    for x in range(szam):
        t.append(random.randint(1,40))
    return t

def bekeres():
    szam = -1
    while (szam < 1):
        szam = int(input())
    return szam


def main():
    n = bekeres()
    t = tombfeltoltes(n)
    print(elsoFKiirasa(t))
    Maosik_feladat(t)
    harmadiFKiirasa(t)
    negyedikfkiiras(t)
main()