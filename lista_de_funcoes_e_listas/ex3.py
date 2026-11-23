# 3 - Concatenação Alternada: Desenvolva uma função que receba duas listas (de
# tamanhos possivelmente diferentes) e retorne uma única lista intercalando os elementos
# de ambas até o fim da menor, adicionando o restante da maior ao final.

l1 = [11, 22, 81]
l2 = [0, 9, 1, 2, 4]

def concatenacao(l1, l2):
    l3 = []

    if len(l1) > len(l2):
        for i in range(len(l2)):
            l3.append(l1[i])
            l3.append(l2[i])

        l3.extend(l1[len(l2):])

    else:
        for i in range(len(l1)):
            l3.append(l1[i])
            l3.append(l2[i])

        l3.extend(l2[len(l1):])

    return l3

print(concatenacao(l1, l2))
