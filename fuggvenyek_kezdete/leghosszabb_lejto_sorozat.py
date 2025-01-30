
def LejtoKiszamitasa(t):
    max_counter = 0
    counter = 1
    for x in range(1,len(t)):
        if t[x] < t[x-1]:
            counter += 1
            if counter >max_counter:
                max_counter = counter
        else:
            counter = 1
    return max_counter
     

def main():
    t = [0, 500, 100, 700, 350, 650, 20, 550, 10, 0]
    print(LejtoKiszamitasa(t))
main()