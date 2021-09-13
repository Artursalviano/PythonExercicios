"""
Próximos Múltipos
Implemente a função ao lado que recebe dois números como parâmetro e retorna, a partir do valor passado,
uma array com os próximos números múltiplos de 7. A quantidade de elementos nessa array deve ser igual ao
segundo número passado na função.

Exemplo: se for passado 5 e 2, deve retornar os próximos 2 múltiplos de 7 a partir do número 5. Nesse caso,
deve retornar a array [7, 14].

Exemplo:se forem passados os números 16 e 3, deve retornar os 3 próximos múltiplos de 7 a partir de 16,
ou seja: [21,28,35]



>>> proximos_multiplos(5, 2)
    [7, 14]

>>> proximos_multiplos(16, 3)
    [21, 28, 35]
"""


def proximos_multiplos(x, y):
    aux = 0
    count = x
    arr = []
    while aux < y:
        count += 1

        if count % 7 == 0:
            arr.append(count)
            aux += 1
    print(arr)

proximos_multiplos(16, 3)