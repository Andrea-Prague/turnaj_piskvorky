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

    if str_jeden_symbol in pole:
        pc_cislo_pole = pole.index(str_jeden_symbol)+1

    elif str_za_jeden_symbol in pole:
        pc_cislo_pole = pole.index(str_za_jeden_symbol)

    elif str_mezera_mezi in pole:
        pc_cislo_pole = pole.index(str_mezera_mezi)

    elif not str_jeden_symbol in pole or not str_za_jeden_symbol in pole:
        while not "-" in pole[pc_cislo_pole]:
            pc_cislo_pole = randrange(len(pole))

    return tah (pole, pc_cislo_pole, symbol)
