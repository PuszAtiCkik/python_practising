
def pozitiv_negativ(szov):
    i = 0
    while i < len(szov):
        if "jó" in szov:
            return "pozitiv"
        else:
            return "negativ"
    i+=1
   
        

def main():
    szoveg = input()
    print(pozitiv_negativ(szoveg))

main()