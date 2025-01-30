
def kulobsegSzamitas(t,limit):
    counter = 0
    for x in range(4,len(t)-1):
        if (t[x + 1] - t[x]) > limit or (t[x] - t[x + 1]) > limit:
            counter += 1
    return counter
    

def main():
    t = [0, 500, 100, 700, 350, 650, 20, 550, 10, 0]
    print(kulobsegSzamitas(t,500))
main()