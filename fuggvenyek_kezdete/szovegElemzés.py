
# def szavak_hossza(text):
#     leghosszab_szo = ""
#     for szo in text:
#         if len(szo) > len(leghosszab_szo):
#             leghosszab_szo = szo
#     return leghosszab_szo

def KeresettSzamElofordulasok(text):
    keresett = 4
    counter = 0
    for x in range(len(text)):
        if text[x] == keresett:
            counter += 1
    return keresett



def szavak_szamlalasa(text):
    counter = 1
    for x in range(len(text)):
        if text[x] == " ":
            counter += 1
    return counter



def main():
    text = "Python is an amazing programming language"
    print(szavak_szamlalasa(text))
    print(KeresettSzamElofordulasok(text))
main()