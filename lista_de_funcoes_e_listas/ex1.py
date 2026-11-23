# # 1 - Média Móvel: Escreva uma função que receba uma lista de números e um número
# # inteiro k (tamanho da janela). A função deve retornar uma lista com as médias de cada
# # sublista contígua de tamanho k.


numbers = [9, 1, 3, 4, 7, 10, 12, 2]
k = 2

def mediamovel(numbers, k):
    medias = []

    for i in range(len(numbers) - k + 1):
        soma = 0

        for j in range(k):
            soma += numbers[i + j]

        media = soma / k
        medias.append(media)

    return medias

resultado = mediamovel(numbers, k)
print(resultado)
