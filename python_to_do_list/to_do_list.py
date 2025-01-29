# import os



# def clear():
#     os.system("cls")


def ToDoListKiirasa(t):
    for index, elem in enumerate(t):  
        print(f"{index + 1}. {elem}")  



def FeladatHozzadasa():
    ToDoist = []
    print("Írj be egy feladatot. Írj 'vége'-t a kilépéshez.")
    feladat = ""  
    while feladat.lower() != "vége":  
        feladat = input("Feladat: ")
        if feladat.lower() != "vége": 
            ToDoist.append(feladat)
    print("Feladatok listája:")
    ToDoListKiirasa(ToDoist)

def UjFeladatInicializalas():
    FeladatHozzadasa()

def FeladatBejeloleseKeszkent():
    print("es")


def elagazas(valasztas):
    if valasztas == "F":
        UjFeladatInicializalas()
    else:
        FeladatBejeloleseKeszkent()

def input_ellenorzes():
    betu = ""
    while (betu != "F" and betu != "D"):
        betu = input("Valassz: ")
    return betu

def main():
    print("Új feladat hozzáadása (F)")
    print("Feladat bejelolese keszkent (D)")
    valasztas = input_ellenorzes().upper()
    elagazas(valasztas)


main()