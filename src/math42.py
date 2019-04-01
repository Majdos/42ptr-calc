import math

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
