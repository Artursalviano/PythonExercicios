def fizz_buzz(n:int):
    '''
    >>> fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz

    :param n:
    :return:
    '''


    for i in range(1, n + 1 ):
        if i%2 == 0 and i%3 == 0:
            print('fizzbuzz')
        else:
            if i%2 == 0:
                print('fizz')
            else:
                if i%3 == 0:
                    print('buzz')
                else:
                    print(i)


fizz_buzz(6)
