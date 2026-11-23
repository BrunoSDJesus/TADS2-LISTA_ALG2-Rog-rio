# Exercício 1: Soma Recursiva de Lista

# Escreva uma função recursiva que receba uma lista de números inteiros e retorne a soma de todos os seus elementos sem utilizar o comando 'sum()' nem laços 'for/while'.

def soma(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma(lista[1:])

print(soma([1, 2, 3, 4, 6, 8, 10]))