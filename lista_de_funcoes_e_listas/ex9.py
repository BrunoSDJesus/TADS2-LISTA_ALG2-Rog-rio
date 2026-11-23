# 9- Escala Crítica de Plantão Médico: Um hospital fornece uma lista onde cada elemento
# é uma sublista com os dias do mês em que um médico específico pode trabalhar. O
# diretor quer saber qual é o dia do mês que tem a menor cobertura de profissionais.
# Retorno exigido: O dia (número) com a menor quantidade de médicos
# disponíveis e uma lista com os índices (IDs) dos médicos que farão plantão
# nesse dia crítico.


escala = [[10, 2, 3], [10, 2, 3], [10, 2, 3], [10, 2, 4]]

def plantao(escala):
    cobertura = {}
    quantidades = []

    for medico in range(len(escala)):
        for dia in escala[medico]:
            if dia in cobertura:
                cobertura[dia] += 1
            else:
                cobertura[dia] = 1
    for quantidade in cobertura.values():
        quantidades.append(quantidade)
    menor = min(quantidades)

    for dia in cobertura:
        if cobertura[dia] == menor:
            dia_critico = dia

    medicos_plantao = []

    for medico in range(len(escala)):
        if dia_critico in escala[medico]:
            medicos_plantao.append(medico)

    return dia_critico, medicos_plantao

dia, medicos = plantao(escala)

print(f"Dia crítico: {dia}")
print(f"IDs dos médicos disponíveis: {medicos}")

plantao(escala)