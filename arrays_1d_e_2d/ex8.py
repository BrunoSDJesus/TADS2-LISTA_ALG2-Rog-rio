# 8 - Utilizando o NumPy: (a) Crie uma matriz 4x4 preenchida com números inteiros
# aleatórios entre 10 e 99 (`np.random.randint()`); (b) Calcule a soma de cada linha 
# (axis=1) e a média de cada coluna (axis=0); (c) Altere a forma da matriz (reshape) de
# 4x4 para 2x8 e exiba a nova estrutura.

import numpy as np

matriz = np.random.randint(10, 99, size=(4, 4))
print(matriz)
print(" ")

soma_linhas = matriz.sum(axis=1)
media_colunas = matriz.mean(axis=0)
print(f'soma: {soma_linhas}')
print(f'media: {media_colunas}')
print(" ")

nova = matriz.reshape(2, 8)
print(nova)
