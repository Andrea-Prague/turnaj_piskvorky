from random import randrange
from piskvorky import tah

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
