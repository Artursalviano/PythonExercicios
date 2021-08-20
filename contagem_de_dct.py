def contar_caracteres(s):
    """ Função que conta os carcteres de uma string
    ex:
    >>> contar_caracteres('artur')
    {'a': 1, 'r': 2, 't': 1, 'u': 1}

    :param s:  string a ser executada
    :return: 
    """


    resultado = {}
    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem+=1
        resultado[caracter] = contagem

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('artur'))
    print()
