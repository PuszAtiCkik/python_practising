

def masodikFkiiras(t):
    counter = felesleges_lepesek(t)
    print(f"{counter} szer")

def felesleges_lepesek(t):
    counter = 0
    for x in range(len(t)- 1):
        if (t[x] == "N" and t[x + 1] == "D") or (t[x] == "D" and t[x + 1] == "N") or \
           (t[x] == "K" and t[x + 1] == "E") or (t[x] == "E" and t[x + 1] == "K"):
            counter += 1
    return counter



def elsoFKiiras(t):
    aksi = robirobot_mozgasa(t)
    if aksi <= 0:
        print("nem eleg")
    else:
        print("eleg")


def robirobot_mozgasa(t):
    aksi = 150
    for x in range(len(t)):
        if t[x] != t[x - 1]:
            aksi -= 8
        else:
            aksi -= 5
    return aksi



def main():
  t = ["E", "D", "D", "N", "D", "N", "K", "N", "E", "N", "E", "N", "E", "N", "E", "D", "D", "K", "K", "N"]  
  elsoFKiiras(t)
  masodikFkiiras(t)
  
main()