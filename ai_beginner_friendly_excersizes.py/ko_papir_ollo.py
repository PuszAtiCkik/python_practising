


import random

def pontok(input):
    gep = 0
    player = 0
    eredemeny = kiNyert(input)
    if eredemeny == "Játékos nyert!":
        player += 1
    else:
        gep += 1
    return gep, player

def kiNyert(jatekos_valasz):
    gep_valas = gep_valasza()
    print(f"A gép választása: {gep_valas}")  

    if jatekos_valasz == "ko" and gep_valas == "ollo":
        return "Játékos nyert!"
    elif jatekos_valasz == "papir" and gep_valas == "ko":
        return "Játékos nyert!"
    elif jatekos_valasz == "ollo" and gep_valas == "papir":
        return "Játékos nyert!"
    elif jatekos_valasz == gep_valas:
        return "Döntetlen!"
    else:
        return "Gép nyert!"

def ellenorzes():
    user_input = input("Válassz: ko, papir vagy ollo: ").strip().lower()
    if user_input not in ["ko", "papir", "ollo"]:
        return "hiba"
    return user_input

def gep_valasza():
    lista = ["ko", "papir", "ollo"]
    return random.choice(lista)

def main():
    jatekos_valasz = ellenorzes()
    if jatekos_valasz == "hiba":
        print("Hibás bemenet! Próbáld újra.")
    else:
        print(kiNyert(jatekos_valasz))
    print(pontok(jatekos_valasz))

main()
