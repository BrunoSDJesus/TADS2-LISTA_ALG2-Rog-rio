# 6 - Sistema de Alerta de Manutenção de Frota: Um ônibus transmite diariamente a
# quilometragem percorrida. Você receberá uma lista com esses trajetos diários e o limite
# de quilometragem para a revisão do motor.
# Instituto Federal de Mato Grosso do Sul
# Lista de Exercícios
# Retorno exigido: A quilometragem total acumulada, o dia (índice da lista) em
# que o limite foi ultrapassado, e um booleano (True ou False) indicando se o
# ônibus precisa ser recolhido imediatamente.


def manutencao(trajetos, limite):
    soma = 0
    recolher = False
    dia_limite = None

    for i in range(len(trajetos)):
        soma += trajetos[i]

        if soma >= limite:
            recolher = True
            dia_limite = i
            return soma, dia_limite, recolher

    return soma, dia_limite, recolher

trajetos = [100, 330, 900, 1100, 50, 976, 43]
limite = 2111

kmTotal, dia, recolher = manutencao(trajetos, limite)

print(f"KM TOTAL: {kmTotal}KM. DIA: {dia}. O CAMINHÃO DEVE SER RECOLHIDO ? {recolher}")