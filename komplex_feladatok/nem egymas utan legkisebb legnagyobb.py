
def egymas_mellet_e(t):
    legkisebb = legkisebb_megkeresese(t)
    legnagyobb = legnagyobb_megkeresese(t)
    for x in range(len(t) - 1):
        if (t[x] == legkisebb and t[x + 1] == legnagyobb) or (t[x] == legnagyobb and t[x + 1] == legkisebb):
            
            return  # Ha megtaláljuk, kiírjuk és kilépünk
    return legkisebb,legnagyobb

def legnagyobb_megkeresese(t):
    max = t[0]
    for x in range(len(t)):
        if t[x] > max:
            max = t[x]
    return max

def legkisebb_megkeresese(t):
    min = t[0]
    for x in range(len(t)):
        if t[x] < min:
            min = t[x]
    return min

def main():
    t = [5, 2, 9, 5, 7,1, 8]
    print(egymas_mellet_e(t))

main()