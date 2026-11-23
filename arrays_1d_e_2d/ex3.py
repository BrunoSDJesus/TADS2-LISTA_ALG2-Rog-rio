# 3 - Crie um vetor com 10 números inteiros de 1 a 10. Utilizando a técnica de fatiamento
# (slicing) do Python: (a) Gere uma sublista contendo apenas os elementos localizados
# nos índices pares; (b) Gere uma sublista contendo apenas os números ímpares (por
# valor); (c) Crie uma cópia da lista inteira invertida sem utilizar o método `.reverse()`.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numeros_pares = []
# numeros_pares.append(nums[1:10:2])
# numeros_impares = []
# numeros_impares.append(nums[0:10:2])

elementos_indices_pares = []
elementos_indices_pares = (nums[0:10:2])

print(elementos_indices_pares)


numeros_impares_porvalor = []
for i in nums:
    if i % 2 != 0:
        numeros_impares_porvalor.append(i) 
print(numeros_impares_porvalor)

lista_invertida = nums[::-1]
print(lista_invertida)

# print(numeros_pares)
# print(numeros_impares)