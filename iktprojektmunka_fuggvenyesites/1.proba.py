

def elso_feladat():
    print("Két szám összeadása")
    try:
        num1 = float(input("Adja meg az első számot: "))
        num2 = float(input("Adja meg a második számot: "))
        print(f"A két szám összege: {num1 + num2}")
    except ValueError:
        print("Érvénytelen számformátum. Próbálja újra!")

def masodik_feladat():
    print("Szöveg megfordítása")
    text = input("Adja meg a szöveget: ")
    print(f"A megfordított szöveg: {text[::-1]}")

def harmadik_feladat():
    print("Lista rendezése")
    try:
        elements = input("Adjon meg számokat vesszővel elválasztva (pl. 5,3,8,1): ")
        num_list = [int(x.strip()) for x in elements.split(",")]
        print(f"Rendezett lista: {sorted(num_list)}")
    except ValueError:
        print("Hiba: Csak számokat adjon meg, vesszővel elválasztva!")

def kilepes():
    print("Kilépés a programból. Viszlát!")
    exit()

def fomenu():
    while True:
        print("Főmenü")
        print("1. Összeadás két szám között")
        print("2. Szöveg megfordítása")
        print("3. Lista elemeinek rendezése")
        print("4. Kilépés")
        
        choice = input("Válasszon egy menüpontot (1-4): ")

        if choice == "1":
            elso_feladat()
        elif choice == "2":
            masodik_feladat()
        elif choice == "3":
            harmadik_feladat()
        elif choice == "4":
            kilepes()
        else:
            print("Érvénytelen választás. Próbálja újra!")




    
    
        
    
        
    

    
    
    
fomenu()