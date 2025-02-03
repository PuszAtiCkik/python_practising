
def kiiras (t):
    max_counter,max_start = leghosszabbNyerosorozat(t)
    
    print(f"A {max_start + 1} es {max_start + max_counter} kozott volt {max_counter} héten keresztul")


def leghosszabbNyerosorozat(t):
    current_start = -1
    max_counter = 0
    counter = 0
    max_start = -1

    for x in range(len(t)):
        if t[x] > 0:
            if counter == 0:
                current_start = x
            counter += 1
            if counter > max_counter:
                max_counter = counter
                max_start = current_start
        else:
            counter = 0
    
    return max_counter, max_start
        


def main():
    t = [6400, -2000, -4300, 8200, 1000, 3400, 600, -900]
    kiiras(t)
main()