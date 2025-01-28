import random




def elsofeladat_szorzo(number,limit):
    for i in range(1, limit + 1):
            print(f"{number} x {i} = {number * i}")

def elsofeladat():
    print("Szorzótábla generálása")
    try:
        number = int(input("Adjon meg egy számot, amelynek a szorzótábláját generáljuk: "))
        limit = int(input("Meddig készüljön a szorzótábla (pl. 10): "))
        elsofeladat_szorzo(number,limit) 
    except ValueError:
        print("Hiba: Csak egész számokat adjon meg!")


def masodik_szavak_megszamlalasa(text):
    words = text.split()
    word_count = len(words)
    return word_count

def masodik_egyedi_szavak(text):
    words = text.split()
    unique_words = set(words)
    return unique_words



def masodik_feladat():
    print("Szavak számlálása szövegben")
    text = input("Írjon be egy szöveget: ")
    word_count = masodik_szavak_megszamlalasa(text)
    print(f"A megadott szövegben {word_count} szó található.")
    unique_words = masodik_egyedi_szavak(text)
    print(f"Az egyedi szavak száma: {len(unique_words)}")
    print("Az egyedi szavak:", ", ".join(unique_words))


def harmadik_feladat_randomszamok(min_val,max_val,n):
    random_numbers = [random.randint(min_val, max_val) for _ in range(n)]
    return random_numbers

def harm_f_fajl_configuracio():
    filename = "random_numbers.txt"
    return filename



def fajl_megnyitas(filename,random_numbers):
    with open(filename, "w") as file:
            file.write("\n".join(map(str, random_numbers)))

def fajl_beolvasasa(filename):
    with open(filename, "r") as file:
            for line in file:
                print(line.strip())


def harmadik_feladat():
    print("Véletlenszámok kezelése fájlban")
    try:
        n = int(input("Hány véletlenszámot generáljon (pl. 10): "))
        min_val = int(input("Adja meg a legkisebb számot: "))
        max_val = int(input("Adja meg a legnagyobb számot: "))
        filename = harm_f_fajl_configuracio()
        random_numbers = harmadik_feladat_randomszamok(min_val,max_val,n)
        
        fajl_megnyitas(filename,random_numbers)
        print(f"A véletlenszámokat elmentettük a(z) {filename} fájlba.")
        
        # Fájl beolvasása
        fajl_beolvasasa(filename)
    except ValueError:
        print("Hiba: Csak egész számokat adjon meg!")
    except Exception as e:
        print(f"Hiba történt: {e}")


def negyedik_f_tippeles():
    try:
        return int(input("Tippelje meg a számot: "))
    except ValueError:
        print("Hiba: Érvényes számot adjon meg!")
        return None

def szamkitalalo_segitseg(guess,secret_number,attempts):
    if guess < secret_number:
                print("A szám nagyobb.")
    elif guess > secret_number:
        print("A szám kisebb.")
    else:
        print(f"Gratulálunk! Kitalálta a számot {attempts} próbálkozás után.")
        exit()

def negyedik_feladat():
    print("Számkitalálós játék")
    try:
        lower = int(input("Adja meg az alsó határt: "))
        upper = int(input("Adja meg a felső határt: "))
        secret_number = random.randint(lower, upper)
        attempts = 0
        print(f"Kitalálandó szám {lower} és {upper} között.")
        while True:
            guess = negyedik_f_tippeles()
            if guess is None:
                continue
            attempts += 1
            szamkitalalo_segitseg(guess,secret_number,attempts)
            
    except ValueError:
        print("Hiba: Csak egész számokat adjon meg!")
    except Exception as e:
        print(f"Hiba történt: {e}")



def fomenu():
    while True:
        print("Főmenü")
        print("1. Matek: Szorzótábla generálása")
        print("2. Szövegkezelés: Szavak számlálása szövegben")
        print("3. Adatkezelés: Véletlenszámok generálása fájlba és olvasása")
        print("4. Játék: Számkitalálós játék")
        print("5. Kilépés")
        
        choice = input("Válasszon egy menüpontot (1-5): ")

        if choice == "1":
            elsofeladat()
        elif choice == "2":
            masodik_feladat()
        elif choice == "3":
            harmadik_feladat()
        elif choice == "4":
            negyedik_feladat()


fomenu()