import re

import math


def addition(x: float, y: float) -> float:
    """Vypocita sucet cisel x a y

        >>> addition(5, 10)
        15

        :param x: prvy operand
        :param y: druhy operand
        :return: sucet dvoch operandov
    """

    return x + y


def subtract(x: float, y: float) -> float:
    """Vypocita rozdiel cisel x a y

        :param x: prvy operand
        :param y: druhy operand
        :return: rozdiel dvoch operandov
    """

    return x - y


def negate(x: float) -> float:
    """Zneguje cislo x

        :param x: cislo na znegovanie
        :return: znegovane cislo
    """

    return -x


def multiplication(x: float, y: float) -> float:
    """Vypocita sucin dvoch cisel x a y

        :param x: prvy cinitel
        :param y: druhy cinitel
        :return: sucin dvoch cinitelov
    """

    return x * y


def division(x: float, y: float) -> float:
    """Vypocita podiel dvoch cisel x a y

        :param x: delenec
        :param y: delitel
        :return: podiel delenca a delitela
        :raises ValueError ak y je 0
    """
    if y == 0:
        raise ValueError('Delenie nulou nie je povolene!')

    return float(x) / y


def factorial(x: int) -> int:
    """Vypocita factorial cisla x

        :param x: cislo pre vypocet faktorialu
        :return: hodnota faktorialu
        :raises ValueError: ak x je negativne alebo nie je prirodzene
    """

    return math.factorial(x)


def absolute_number(x: float) -> float:
    """Vypocita absolutnu hodnotu zadaneho cisla
        :param x: cislo pre vypocet absolutnej hodnoty
        :return: cislo x vratene v absolutnej hodnote
    """

    if x < 0:
        return x * (-1)

    return x


def natural_exponent(x: float) -> float:
    """Vypocita pre cislo x funkciu e^x
        :param x: cislo pre vypocet e^x
        :return: vysledok danej funkcie pre x
    """

    return math.exp(x)


def ln(x: float) -> float:
    """Vypocita prirodzeny logaritmus zadaneho cisla
        :param x: cislo pre vypocet prir. logaritmu
        :return: vrati vysledok pre prir. logaritmus zadaneho cisla
        :raises ValueError: ak argument je negativny alebo 0
    """

    if x <= 0:
        raise ValueError('Zadane cislo musi byt vacsie ako 0!')

    return math.log(x)


def sqrt(x: float) -> float:
    """Vypocita obecnu odmocninu (druhu odmocninu) z cisla x
        :param x: cislo pre vypocet obecnej odmocniny
        :return: Obecna odmocnina cisla x
        :raises ValueError ak argument je negativny
    """

    if x < 0:
        raise ValueError('Zadane cislo musi byt vacsie alebo rovne 0!')

    return math.sqrt(x)


def root(x: float, y: float) -> float:
    """Vypocita y-ntu odmocninu z cisla x
        :param x: cislo z ktoreho chceme odmocninu
        :param y: kolka odmocnina
        :return: Y-nta odmocnina z x
    """

    if x < 0:
        raise ValueError('Zadane cislo "X" musi byt vacsie alebo rovne 0!')

    if y <= 0:
        raise ValueError('Zadane cislo "Y" musi byt vacsie ako 0!')

    return math.pow(x, (1 / y))


def bin_to_dec(xb: str) -> int:
    """Premeni binarne cislo na dekadicke
        :param xb: binarne cislo
        :return: Dekadicke cislo z binarneho vstupu
        :raises ValueError ak xb nie je cislo v binarnom tvare
    """

    is_bin = re.match(r"^[01]+$", xb)

    if is_bin:
        binary_num = int(xb, 2)
        return binary_num
    else:
        raise ValueError('Zadane cislo musi byt zadane v binarnom tvare!')


def hex_to_dec(xh: str) -> int:
    """Premeni hexadecimalne cislo na dekadicke
        :param xh: hexadecimalne cislo
        :return: Dekadicke cislo z hexadecimalneho vstupu
        :raises ValueError ak xb nie je cislo v hexadecimalnom tvare
    """

    is_hex = re.match(r"^[0-9A-F]+$", xh, re.IGNORECASE)

    if is_hex:
        hex_num = int(xh, 16)
        return hex_num
    else:
        raise ValueError(
            'Zadane cislo musi byt zadane v hexadecimalnom tvare!')


def oct_to_dec(xo: str) -> int:
    """Premeni oktalove cislo na dekadicke
        :param xo: oktalove cislo
        :return: Dekadicke cislo z oktaloveho vstupu
        :raises ValueError ak xb nie je cislo v oktalovom tvare
    """

    is_oct = re.match(r"^[0-7]+$", xo)

    if is_oct:
        oct_num = int(xo, 8)
        return oct_num
    else:
        raise ValueError(
            'Zadane cislo musi byt zadane v oktalovom tvare!')
