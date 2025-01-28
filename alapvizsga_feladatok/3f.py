class Gokart:
    def __init__(self, nev, telepules, palya_hossz, jegyar):
        self.nev = nev
        self.telepules = telepules
        self.palya_hossz = int(palya_hossz)
        self.jegyar = int(jegyar)

palyak_hossz = 0
gokartok = []
min = None
min_jegyar_nev = None


with open("alapvizsga_feladatok/gokart.txt", "r", encoding="utf-8") as basefile:
    for sor in basefile:
        
        sor = sor.strip()  # Sor eleji és végi whitespace eltávolítása
        if sor:  # Csak nem üres sorok feldolgozása
            adatok = sor.split(";")  # Az adatokat pontosvessző mentén feldaraboljuk
            gokart = Gokart(adatok[0], adatok[1], adatok[2], adatok[3])  # Példányosítjuk az osztályt
            gokartok.append(gokart)  # Hozzáadjuk a listához
            palyak_hossz += gokart.palya_hossz
            if min is None or gokart.jegyar < min:
                min = gokart.jegyar
                min_jegyar_nev = gokart.nev

print(min)
print(min_jegyar_nev)
print(palyak_hossz)

