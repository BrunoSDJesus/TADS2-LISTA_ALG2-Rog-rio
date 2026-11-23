# 4 - Merge de Listas Ordenadas: Desenvolva uma função que receba duas listas que já
# estão ordenadas de forma crescente. A função deve retornar uma única lista contendo
# todos os elementos de ambas, também ordenada. Não é permitido concatenar e aplicar
# algoritmo de ordenação depois.

l1 = [1, 3, 5, 11]
l2 = [2, 4, 6, 8, 9]


def merge(l1, l2):
    i = 0
    z = 0
    l3 = []
    while i < len(l1) and z < len(l2):
        if l1[i] < l2[z]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[z])
            z += 1
        if i > len(l1):
            l3.append(l1[i])
        elif (z > len(l2)):
            l3.append(l2[z])

  
    return l3
   

print(merge(l1, l2))
