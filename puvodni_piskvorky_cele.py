from random import randrange

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah(pole, cislo_pole, symbol):
    return pole[:cislo_pole] + symbol + pole[cislo_pole + 1:]

def tah_hrace (pole, symbol):
    while True:
        cislo_pole = int (input ("zadej cislo pole, kde chces udelat tah "))
        if cislo_pole <0:
            print ("nelze zadat zaporne cislo, zkus to znovu")
        elif cislo_pole > len(pole)-1:
            print ("moc vysoke cislo, zkus to znovu")
        elif "-" not in pole[cislo_pole]:
            print ("toto pole je obsazene, zkus to znovu")
        else:
            return tah(pole, cislo_pole,symbol)

def tah_pocitace(pole):
    pc_cislo_pole = randrange(len(pole))
    while not "-" in pole[pc_cislo_pole]:
        pc_cislo_pole = randrange(len(pole))
    return tah (pole, pc_cislo_pole, "o")

def piskovrky1d():
    pole = "-" * 20
    symbol = input("Zadej znak, ktery chces pouzivat ")
    while "-" in pole:
            pole = tah_hrace(pole, symbol)

            if vyhodnot(pole) == "x":
                print (pole)
                print ("uzivatel vyhral")
                break

            pole = tah_pocitace(pole)
            print (pole)

            if vyhodnot(pole) == "o":
                print ("PC vyhral")
                break

    if vyhodnot(pole) == "!":
        print ("remiza")

piskovrky1d()
