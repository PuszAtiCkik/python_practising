import random
def gép_válasza(e):
    return random.choice(e[0:3])

def döntés(a,b):
    if a == b:
        print("döntetlen")
    elif a == "fleksz":
        print("nyertél")
    elif (a == "ko" and b == "papir") or (a == "papir" and b == "olló") or (a == "olló" and b == "ko"):
        print("vesztettel")
    else:
        print("nyertél") 

def jatek(e):
    j=""
    while j not in e:
        j = input(f"Mit választasz {e[0:3]}")
    g = gép_válasza(e)
    print(f"A gép válasza : {g}")
    döntés(j,g)




eszkozok = ["ko","papir","ollo","fleksz"]
while True:
    jatek(eszkozok)