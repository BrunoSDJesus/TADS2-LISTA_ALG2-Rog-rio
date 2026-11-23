# 5 - Uma imagem digital é formada por pixels. Você receberá uma lista de tuplas, onde
# cada tupla contém três inteiros (R, G, B) representando as cores Vermelho, Verde e
# Azul de um pixel (valores de 0 a 255).
# Transforme o formato original dos dados convertendo uma tupla de três elementos em
# um único valor inteiro (a média, usando divisão inteira), além de identificar uma
# condição específica absoluta.
# Crie uma nova lista contendo a média inteira de cada tupla e um contador informando
# quantos pixels da imagem original eram puramente pretos (0, 0, 0).
# Na Main: Crie uma lista simulando os pixels de uma foto pequena, garantindo que
# contenha pelo menos um ou dois pixels totalmente pretos e outros variados. Passe essa
# lista para a função e imprima a nova "imagem" processada, além do relatório
# informando a quantidade exata de pixels escuros puros encontrados.

def main():
    pixels = [
        (1, 1, 1),
        (0, 0, 0),
        (0, 0, 0),
        (12, 122, 244),
        (0, 1, 0),
        (51, 64, 61),
        (255, 255, 255)
    ]

    medias, pixel_preto = imagem(pixels)
    print(f"Imagem {medias}, pixels pretos : {pixel_preto}")

def imagem(pixels):
    media = 0
    medias = []
    pixel_preto = 0
    for pixel in pixels:
        media = (pixel[0] + pixel[1] + pixel[2]) // 3
        medias.append(media)
        if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
            pixel_preto += 1

    return medias, pixel_preto

main()
    