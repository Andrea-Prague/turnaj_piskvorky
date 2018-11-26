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

def tah_pocitace(pole, symbol):
    pc_cislo_pole= randrange(len(pole))
    jeden_symbol = [symbol, "-"]
    str_jeden_symbol = "".join(jeden_symbol)

    za_jeden_symbol =  ["-", symbol]
    str_za_jeden_symbol = "".join(za_jeden_symbol)

    mezera_mezi = [symbol, "-", symbol]
    str_mezera_mezi = "".join(mezera_mezi)

    if not "x" in symbol and "x" in pole:
        if str_jeden_symbol in pole:
            pc_cislo_pole = pole.index(str_jeden_symbol)+1

        elif str_za_jeden_symbol in pole:
            pc_cislo_pole = pole.index(str_za_jeden_symbol)

        elif str_mezera_mezi in pole:
            pc_cislo_pole = pole.index(str_mezera_mezi)

        elif "xx-" in pole:
            pc_cislo_pole = pole.index("xx-")+2

        elif "-xx" in pole:
            pc_cislo_pole = pole.index("-xx")+2

        elif not str_jeden_symbol in pole or not str_za_jeden_symbol in pole:
            pc_cislo_pole = randrange(len(pole))
        while not "-" in pole[pc_cislo_pole]:
                pc_cislo_pole = randrange(len(pole))

    elif not "o" in symbol and "o" in pole:
        if str_jeden_symbol in pole:
            pc_cislo_pole = pole.index(str_jeden_symbol)+1

        elif str_za_jeden_symbol in pole:
            pc_cislo_pole = pole.index(str_za_jeden_symbol)

        elif str_mezera_mezi in pole:
            pc_cislo_pole = pole.index(str_mezera_mezi)

        elif "oo-" in pole:
            pc_cislo_pole = pole.index("oo-")+2

        elif "-oo" in pole:
            pc_cislo_pole = pole.index("-oo")+2

        elif not str_jeden_symbol in pole or not str_za_jeden_symbol in pole:
            pc_cislo_pole = randrange(len(pole))
        while not "-" in pole[pc_cislo_pole]:
                pc_cislo_pole = randrange(len(pole))

    return tah (pole, pc_cislo_pole, symbol)


def piskovrky1d():
    pole = "-" * 20
    symbol = input("Zadej znak, ktery chces pouzivat ")
    while "-" in pole:
            pole = tah_hrace(pole, symbol)

            if vyhodnot(pole) == "x":
                print (pole)
                print ("uzivatel vyhral")
                break

            pole = tah_pocitace(pole, "o")
            print (pole)

            if vyhodnot(pole) == "o":
                print ("PC vyhral")
                break

    if vyhodnot(pole) == "!":
        print ("remiza")

piskovrky1d()
