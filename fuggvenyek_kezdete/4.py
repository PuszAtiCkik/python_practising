def even(number):
    if number % 2 == 0:
        return True
    

    
def main():
    szam = int(input())
    if even(szam):
        print("paros")
    else:
        print("gatyaq")

main()