
def muvelet_valaszto():
    valasztott = input("Válassz egy műveletet (+, -, *, /): ")
    while valasztott not in ["*", "+", "-", "/"]:
        print("Érvénytelen művelet! Kérlek, válassz egyet a következők közül: +, -, *, /")
        valasztott = input("Válassz egy műveletet (+, -, *, /): ")
    return valasztott

def szam_ellenorzes():
    szam = int(input())
    while (szam < 1):
        szam = int(input())
    return szam

def muvelet_utani_valasztas(character,elso_szam,masodik_szam):
    if character == "+":
        return osszeadas(elso_szam,masodik_szam)
    elif character == "-":
        return kivonas(elso_szam,masodik_szam) 
    elif character == "/":
        return osztas(elso_szam,masodik_szam) 
    elif character == "*":
        return szorzas(elso_szam,masodik_szam) 

def osszeadas(elsosz,masodiksz):
    return elsosz + masodiksz

def kivonas(elsosz,masodiksz):
    if elsosz > masodiksz:
        eredmeny = elsosz - masodiksz
    else:
        eredmeny = masodiksz - elsosz
    return eredmeny

def osztas(elsosz,masodiksz):
    if masodiksz == 0:
        print("nullaval nem lehet oszttani")
        return None
    return elsosz / masodiksz

def szorzas(elsosz,masodiksz):
    return elsosz * masodiksz

def main():
    print("koszontelek a szamologepbe")
    print("muvelet (+ - / *)")
    muvelet = muvelet_valaszto()
    print("elso szam")
    elso_szam = szam_ellenorzes()
    print("masodik szam")
    masodik_szam = szam_ellenorzes()
    eredmeny = muvelet_utani_valasztas(muvelet,elso_szam,masodik_szam)
    if eredmeny is not None:
        print(f"Eredmény {eredmeny}")
    
    
main()