# 2 - Deslocamento (Shift) à Direita: Crie uma função que receba uma lista e um inteiro n.
# A função deve retornar uma nova lista com os elementos deslocados n posições para a
# direita. Os elementos que "saírem" do final devem reaparecer no início.


numeros = [1, 2, 3, 4, 5, 6]
n = 2

def shift(numeros, n):
    lista = [None] * len(numeros)

    for i in range(len(numeros)):
        calc = (i + n) % len(numeros)
        lista[calc] = numeros[i]

    return lista

resultado = shift(numeros, n)
print(resultado)
