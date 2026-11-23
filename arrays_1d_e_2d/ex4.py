# 4 - Utilizando a biblioteca NumPy: (a) Crie um array 1D com os números inteiros de 10
# a 50 (inclusive) com passo 5 usando `np.arange()`; (b) Eleve todos os elementos do
# array ao quadrado de forma vetorizada (sem laço `for`); (c) Aplique uma filtragem por
# indexação booleana para extrair apenas os valores superiores a 500.

import numpy as np

nums = np.arange(10, 51, 5)

print(nums)

quadrado = (nums ** 2)

print(quadrado)

maior_500 = quadrado[quadrado > 500]

print(maior_500)