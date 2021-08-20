def rotate_array(l, k):
    '''
    >>> rotate_array([1,2,3,4,5,6,7], 3)
    [5, 6, 7, 1, 2, 3, 4]

    :param l:
    :param k:
    :return:
    '''

    a = l[0:-k]
    b = l[k+1:]

    a.reverse()
    b.reverse()

    resultado = a + b
    resultado.reverse()



    return print(resultado)

rotate_array([1,2,3,4,5,6,7],3)