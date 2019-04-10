import math
import re


def addition(x, y):
    """Vypocita sucet cisel x a y

        >>> addition(5, 10)
        15

        :param x: prvy operand
        :param y: druhy operand
        :return: sucet dvoch operandov
    """

    return x+y


def subtract(x, y):
    """Vypocita rozdiel cisel x a y

        :param x: prvy operand
        :param y: druhy operand
        :return: rozdiel dvoch operandov
    """

    return x-y


def multiplication(x, y):
    """Vypocita sucin dvoch cisel x a y

        :param x: prvy cinitel
        :param y: druhy cinitel
        :return: sucin dvoch cinitelov
    """

    return x*y


def division(x, y):
    """Vypocita podiel dvoch cisel x a y

        :param x: delenec
        :param y: delitel
        :return: podiel delenca a delitela
    """
    if y == 0:
        raise ValueError('Delenie nulou nie je povolene!')

    return float(x)/y


def factorial(x):
    """Vypocita factorial cisla x

        :param x: cislo pre vypocet faktorialu
        :return: hodnota faktorialu
    """

    return math.factorial(x)


def absoluteNumber(x):
    """Vypocita absolutnu hodnotu zadaneho cisla
        :param x: cislo pre vypocet absolutnej hodnoty
        :return: cislo x vratene v absolutnej hodnote
    """

    if x < 0:
        return x*(-1)

    return x


def naturalExponent(x):
    """Vypocita pre cislo x funkciu e^x
        :param x: cislo pre vypocet e^x
        :return: vysledok danej funkcie pre x
    """

    return math.exp(x)


def ln(x):
    """Vypocita prirodzeny logaritmus zadaneho cisla
        :param x: cislo pre vypocet prir. logaritmu
        :return: vrati vysledok pre prir. logaritmus zadaneho cisla
    """

    if x <= 0:
        raise ValueError('Zadane cislo musi byt vacsie ako 0!')

    return math.log(x)


def sqrt(x):
    """Vypocita obecnu odmocninu (druhu odmocninu) z cisla x
        :param x: cislo pre vypocet obecnej odmocniny
        :return: Obecna odmocnina cisla x
    """

    if x < 0:
        raise ValueError('Zadane cislo musi byt vacsie alebo rovne 0!')

    return math.sqrt(x)


def root(x, y):
    """Vypocita y-ntu odmocninu z cisla x
        :param x: cislo z ktoreho chceme odmocninu
        :param y: kolka odmocnina
        :return: Y-nta odmocnina z x
    """

    if x < 0:
        raise ValueError('Zadane cislo "X" musi byt vacsie alebo rovne 0!')

    if y <= 0:
        raise ValueError('Zadane cislo "Y" musi byt vacsie ako 0!')

    return math.pow(x, (1/y))


def binToDec(xb):
    """Premeni binarne cislo na dekadicke
        :param xb: binarne cislo
        :return: Dekadicke cislo z binarneho vstupu
    """

    is_bin = re.match('^[01]+$', xb)

    if is_bin:
        binary_num = int(xb, 2)
        return binary_num
    else:
        raise ValueError('Zadane cislo musi byt zadane v binarnom tvare!')


def hextoDec(xh):
    """Premeni hexadecimalne cislo na dekadicke
        :param xh: hexadecimalne cislo
        :return: Dekadicke cislo z hexadecimalneho vstupu
    """

    is_hex = re.match('^[0-9A-F]+$', xh, re.IGNORECASE)

    if is_hex:
        hex_num = int(xh, 16)
        return hex_num
    else:
        raise ValueError(
            'Zadane cislo musi byt zadane v hexadecimalnom tvare!')


def octToDec(xo):
    """Premeni oktalove cislo na dekadicke
        :param xo: oktalove cislo
        :return: Dekadicke cislo z oktaloveho vstupu
    """

    is_oct = re.match('^[0-7]+$', xo)

    if is_oct:
        oct_num = int(xo, 8)
        return oct_num
    else:
        raise ValueError(
            'Zadane cislo musi byt zadane v oktalovom tvare!')
