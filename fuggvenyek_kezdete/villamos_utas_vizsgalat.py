def UtasFeLeVizsgalat(t):
    minden_jo = True  

    for x in range(0,len(t) - 1):  
        if t[x] < t[x + 1]:  
            minden_jo = False  

    if minden_jo:
        print("Igaz, hogy mindig több szállt fel, mint le!")
    else:
        print("Nem igaz, hogy mindig több szállt fel, mint le!")

def main():
    t1 = [2, 0, 4, 1, 15, 11, 22, 14, 16, 2, 0, 31]
    print("Bemenet:", t1)
    UtasFeLeVizsgalat(t1)  

    
    

main()
