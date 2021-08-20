def contar_caracteres(s):
    """ Função que conta os carcteres de uma string
    ex:
    >>> contar_caracteres('Artur')
    A: 1
    r: 2
    t: 1
    u: 1
    :param s:  string a ser executada
    :return: 
    """
    caracteres_ordenados = sorted(s)
    caractere_anterior = caracteres_ordenados[0]
    contagem = 1
    for caracter in caracteres_ordenados[1:]:
        if caracter == caractere_anterior:
            contagem += 1
        else:
            print(f'{caractere_anterior}: {contagem}')
            caractere_anterior = caracter
            contagem = 1
    print(f'{caractere_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracteres('Artur')
    print()
