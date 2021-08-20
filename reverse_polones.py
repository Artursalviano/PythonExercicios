import operator

operador = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def reverse_polones(lista):
    """
    >>> reverse_polones(["2", "1", "+", "3", "*"])
    9

    :param lista:
    :return:
    """
    lista_2 = []

    for chave in lista:
        if chave in operador:
            x = lista_2.pop()
            y = lista_2.pop()
            resultado = operador[chave](y, x)
            lista_2.append(int(resultado))
        else:
            lista_2.append(int(chave))
    return lista_2.pop()


print(reverse_polones(["2", "1", "+", "3", "*"]))
print(reverse_polones( ["4", "13", "5", "/", "+"]))





