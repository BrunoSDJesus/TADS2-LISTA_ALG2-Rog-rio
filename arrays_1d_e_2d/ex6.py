# 6 - Construa um programa em Python nativo para ler uma matriz 3x3 de inteiros
# digitados pelo usuário: (a) Preencha a matriz utilizando laços aninhados em listas de
# listas (`list[list]`); (b) Imprima a matriz em formato tabular formatado; (c) Exiba os
# elementos da diagonal principal (onde índice da linha i == coluna j) e da diagonal
# secundária (onde i + j == 2).


matriz1 = []

for i in range(3):
    linha = []

    for j in range(3):
        n = int(input("digite um numero: "))
        linha.append(n)

    matriz1.append(linha)

for i in range(3):
    for j in range(3):
        print(matriz1[i][j], end=" ")
    print()
print('diagonal principla')
for i in range(3):
    for j in range(3):
        if i == j:
            print(matriz1[i][j])
print('segundaria')
for i in range(3):
    for j in range(3):
        if i + j == 2:
            print(matriz1[i][j])
