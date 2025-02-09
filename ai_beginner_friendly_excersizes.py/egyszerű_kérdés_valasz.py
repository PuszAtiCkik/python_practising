from datetime import datetime


def hogy_vagy_kerdesek():
    return "jol koszi"

def mai_nap_kerdes():
    today = datetime.today().strftime('%A')
    return today


def valaszto(inp):
    if "hogy vagy" in inp.lower():
        return hogy_vagy_kerdesek()
    elif "milyen nap van" in inp.lower():
        return mai_nap_kerdes()
    else:
        return "nem értem a szoveget"
    

def main():
    user_input = input()
    print(valaszto(user_input))

main()