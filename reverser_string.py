def reverse_string(s:str):
    """
    >>> reverse_string('artur iury')
    'iury artur'

    >>> reverse_string('artur iury de almeida salviano')
    'salviano almeida de iury artur'

    :param s:
    :return:
    """
    lista_s = s.split()
    lista_s.reverse()
    resultado = ' '.join(lista_s)

    return resultado
