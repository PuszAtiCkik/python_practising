# 3 adat elso melyik nap masodik hanyadik fuvar az utso pedig hany km tett meg
# 0-5: 1000
# 6-10:1800
# 11-15:2100
# 16-20:2300
# 21- : 2500
# 1. a hét elso fuvarja hany km kesz
# 2. a het utolso fuvarja hany km kesz
# 3. a hét melyik nap nem dolgozott kesz
# 4.hanyadik fuvar volt a fajla amiert legtobb penzt kapta (elso) kesz
# 5. melyik nap kereste a legkevesebbet
# 6. melyik nap dolgozta a legtobbet kesz 





def MelyikNapLEGKEVESEBBpenz(t):
    osszegek = NapokKmOsszeadasa(t)

    min_ertek = osszegek[0]
    min_index=0


    i=1
    while i < len(osszegek):
        if osszegek[i] < min_ertek:
            min_ertek = osszegek[i]
            min_index = i
        i+=1
    
    napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
    print(napok[min_index])


def NapokKmOsszeadasa(t):
    hetfo = 0
    kedd = 0
    szerda = 0
    csut = 0
    pentek = 0
    szombat = 0
    vasarnap = 0
    for nap,_,km in t:
        if nap == 1:
            hetfo += km
        if nap == 2:
            kedd += km
        if nap == 3:
            szerda += km
        if nap == 4:
            csut += km
        if nap == 5:
            pentek += km
        if nap == 6:
            szombat += km
        if nap == 7:
            vasarnap += km
    return hetfo,kedd,szerda,csut,pentek,szombat,vasarnap
    


def MelyikNapDolgoztaegtobbet(t):
    max_fuvar = 0
    for nap,fuvar,_ in t:
        if fuvar > max_fuvar:
            max_fuvar = fuvar
            legtobbetdolgozottnap = nap
    return legtobbetdolgozottnap

def LegtobbetDolgozott(t):
    legtobb = MelyikNapDolgoztaegtobbet(t)
    print(f"legtobbet dolgozott nap {legtobb}")



def MaximumKivalasztasKmre(t):
    LegtobbKm = 0
    for nap,_,km in t:
        if km > LegtobbKm:
            LegtobbKm = km
            Melyiknaplegtobb = nap
    return Melyiknaplegtobb, LegtobbKm



def LegtobbPenz(t):
    MostMoneyDay, legtobbkm = MaximumKivalasztasKmre(t)
    print(f"legjobban kereso nap {MostMoneyDay} ennyi km vel {legtobbkm}")

    



def MaxKivalasztasUtsoHet(t):
    max_fuvar = 0
    for nap,fuvar,_ in t:
        if nap == 7 and fuvar > max_fuvar:
            max_fuvar = fuvar
    return max_fuvar




def HetUtolsoFuvarja(t):
    for nap,fuvar,km in t:
        if nap == 7 and fuvar == MaxKivalasztasUtsoHet(t):
            print(km)
    


def Szabinap(t):
    i=0
    for nap,fuvar,_ in t:
        while i < len(t) and fuvar != 0:
            i+=1
    if i <len(t):
        print(f"volt")
    else:
        print("nem volt")
    

def MinKivalasztas(t):
    min = 8
    for _,fuvar,_ in t:
        if fuvar < min:
            min = fuvar
    return min


def HetELSOFuvarja(t):
    for nap,fuvar,km in t:
        if nap == 1 and fuvar == MinKivalasztas(t):
            print(km)




def ecsr(t):
    for i in range(len(t)-1):
        for y in range(i+1,len(t)):
            if t[i] > t[y]:
                sv = t[i]
                t[i] = t[y]
                t[y] = sv
    return t
    

def TupleHozzaadas():
    tomb = []
    for i in range(61):
        adatok = input().split()
        tomb.append((int(adatok[0]),int(adatok[1]),int(adatok[2])))
    return tomb


def main():
    t = TupleHozzaadas()
    RendezettTomb = ecsr(t)
    print(RendezettTomb)
    HetELSOFuvarja(RendezettTomb)
    Szabinap(RendezettTomb)
    HetUtolsoFuvarja(RendezettTomb)
    LegtobbPenz(RendezettTomb)
    LegtobbetDolgozott(RendezettTomb)
    MelyikNapLEGKEVESEBBpenz(t)
main()