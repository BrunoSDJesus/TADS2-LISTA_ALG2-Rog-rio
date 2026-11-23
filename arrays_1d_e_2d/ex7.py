# 7 - Dada a matriz nativa 3x2 `matriz = [[1, 2], [3, 4], [5, 6]]`: (a) Permita que o usuário
# atualize o valor da linha 1, coluna 0 para 99; (b) Escreva uma função que construa e
# retorne a matriz transposta (tamanho 2x3), onde as linhas da matriz original viram
# colunas.

matriz = [[1, 2], [3, 4], [5, 6]]

for i in range(3):
    for j in range(2):
        print(matriz[i][j], end=" ")
    print()

n = int(input("insira o número 99 para alterar a linha 1 coluna 0 da matriz: "))
if n != 99:
    print("numero errado, faça novamente")

else:
    matriz[1][0] = n

    for i in range(3):
        for j in range(2):
            print(matriz[i][j], end=" ")
        print()

def transposta(matriz):
    result = []
    for j in range(2):                
        linha = []
        for i in range(3):        
            linha.append(matriz[i][j])
        result.append(linha)
    return result

print(transposta(matriz))