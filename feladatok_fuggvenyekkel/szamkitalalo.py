import random




def ellenorzes(tipp,gep):
    
    if tipp > gep:
        return "kisebb"
    elif tipp < gep:
        return "nagyobb"
    else:
        return "eltalaltad"

def szam_generalas():
    return random.randint(1,10)



def bekeres():
    szam = -1
    while szam < 1 or szam > 10:
        szam = int(input())
    return szam

def main():


    gep = szam_generalas()
    print("A játék elkezdődött. Próbálj eltalálni egy számot 1 és 10 között!")
    
    eredmeny = ""  
    while eredmeny != "eltalaltad":
        player_input = bekeres()
        eredmeny = ellenorzes(player_input, gep)
        print(eredmeny)
main()