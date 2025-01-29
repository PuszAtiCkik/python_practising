
def fibonnacci(n):
    fib_elemek = [0,1]
    for x in range(2,n):
        fib_elemek.append(fib_elemek[x - 1] + fib_elemek[x - 2])
    return fib_elemek
         



def main():
    n = 10
    print(fibonnacci(n))
main()