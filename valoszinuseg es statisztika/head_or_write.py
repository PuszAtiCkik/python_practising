import random



def fejgyakorisag(dobasok):
    counter = 0
    for x in range(len(dobasok)):
        if dobasok[x] == "fej":
            counter += 1
    
    return counter / len(dobasok)


def irasgyakorisag(dobasok):
    counter = 0
    for x in range(len(dobasok)):
        if dobasok[x] == "iras":
            counter += 1
    
    return counter / len(dobasok)



dobas = []

for x in range(1000):
    
    dobasok = random.choice(["fej","iras"])
    dobas.append(dobasok)

print(fejgyakorisag(dobas))
print(irasgyakorisag(dobas))

