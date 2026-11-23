# 1 - Uma estufa inteligente possui vários sensores. O microcontrolador envia uma lista
# de tuplas no formato (id_sensor, temperatura, umidade). As regras de segurança dizem
# que a temperatura não pode passar de 35°C e a umidade não pode ficar abaixo de 20%.
# Você precisa rastrear simultaneamente o maior valor de uma variável e o menor de
# outra, enquanto filtra dados.
# Retorno Exigido: Uma lista contendo apenas os id_sensor que dispararam algum
# alarme de perigo, e uma tupla (maior_temperatura, menor_umidade) registrada em todo
# o período.
# Na Main: Crie uma lista simulando pelo menos 4 sensores (certifique-se de forçar pelo
# menos um alerta de temperatura e um de umidade). Chame a função passando essa lista.
# Imprima no terminal quais sensores entraram em alerta e exiba os picos máximos e
# mínimos.


def estufa(microcontrolador):
    ids = []
    maior_temperatura = None
    menor_umidade = None

    for sensor in microcontrolador:
        id_sensor = sensor[0]
        temperatura = sensor[1]
        umidade = sensor[2]

        if temperatura > 35 or umidade < 20:
            ids.append(id_sensor)

        if maior_temperatura is None or temperatura > maior_temperatura:
            maior_temperatura = temperatura

        if menor_umidade is None or umidade < menor_umidade:
            menor_umidade = umidade

    return ids, (maior_temperatura, menor_umidade)


def main():
    microcontrolador = [
        (1, 50, 40),
        (2, 31, 35),
        (3, 21, 1),
        (4, 32, 21)
    ]

    alertas, picos = estufa(microcontrolador)

    print("Sensores em alerta:", alertas)
    print("Maior temperatura e menor umidade:", picos)


main()
