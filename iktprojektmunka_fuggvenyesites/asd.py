t = [3, 37, 18, 38, 3, 3, 28, 27, 39, 40]


counter = 0

lista = []
for x in t:
    if x in lista:
        counter += 1
    else:
        counter = 1
