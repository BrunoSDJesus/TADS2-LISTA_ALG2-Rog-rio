#  - Em um motor gráfico, os obstáculos circulares são uma lista de tuplas (pos_x, pos_y,
# raio). Você recebe também a tupla do jogador (jog_x, jog_y, jog_raio).
# A colisão ocorre se a distância entre os centros (use a soma das diferenças absolutas de
# X e Y como simplificação) for menor que a soma dos raios.
# Retorno Exigido: Um booleano True ou False indicando se o jogador colidiu com
# algum obstáculo e a quantidade exata de obstáculos com os quais ele está colidindo
# simultaneamente.
# Na Main: Defina uma lista com vários obstáculos espalhados pelo mapa e uma variável
# separada para as coordenadas do jogador, forçando uma posição onde ele encoste em
# pelo menos dois obstáculos ao mesmo tempo. Chame a função e exiba uma mensagem
# de status ("Impacto Detectado!" ou "Caminho Livre") e a quantidade de objetos
# atingidos.

def main():
    # x, y raio
    obstaculos = [
        (15, 12, 4),
        (11, 9, 10),
        (1, 2, 4),
        (43, 32, 10),
        (12, 11, 6),
        (10, 5, 2),
        (17, 1, 10),
        (2, 14, 4)
    ]

    jogador = (12, 11, 6)

    colisao, obstaculos_atingidos = motorGrafico(obstaculos, jogador)

    if colisao == True:

        print("Impacto Detectado! ")
        print(f"A quantidade de objetos atingidos é de: {obstaculos_atingidos} ")
    else:
        print("Caminho Livre! ")

def motorGrafico(obstaculos, jogador):
    deltaX = 0
    deltaY = 0
    raios = 0
    distancia = 0
    colisao = False
    obstaculos_atingindos = 0

    for i in range(len(obstaculos)):
        deltaX = abs(jogador[0] - obstaculos[i][0])
        deltaY = abs(jogador[1] - obstaculos[i][1])
        distancia = (deltaX + deltaY)
        raios = (jogador[2] + obstaculos[i][2]) 

        if distancia < raios:
            colisao = True
            obstaculos_atingindos += 1

    return colisao, obstaculos_atingindos

main()