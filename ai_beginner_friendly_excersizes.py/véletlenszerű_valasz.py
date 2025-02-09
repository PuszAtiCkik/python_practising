import random


def megnezni_hogykerdes_e(user_input):
    if "hogy vagy" and "?" in user_input:
        return "koszonom szepen"


def HogyVagyKerdesre():
    lista = ["Jól vagyok!", "Nem túl jól.", "Szuperül!"]
    return lista


def eldontes(user_inp):
    if "hogy vagy" in user_inp.lower():
        erzelem = HogyVagyKerdesre()
        return valasztas(erzelem)
    return "ismeteld meg kerlek"




def valasztas(lehetosegek):
    return random.choice(lehetosegek)

def main():
    user_input = input()
    print(eldontes(user_input))
    print(megnezni_hogykerdes_e(user_input))
main()
