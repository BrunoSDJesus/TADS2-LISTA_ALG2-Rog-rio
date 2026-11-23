# 7 - Análise de Turbulência em Voo: Os sensores de um avião registram a altitude a cada
# minuto (lista de números). Uma turbulência severa é caracterizada por uma queda de
# altitude maior que 500 metros em um único minuto.
# Retorno exigido: True ou False se houve turbulência severa, e a maior queda
# registrada em um minuto durante todo o voo.



altitude = [1000, 1050, 1449, 501, 100, 599, 603, 50]

def turbulencia(altitude):
    turb_severa = False
    maior_queda = 0

    for i in range(1, len(altitude)):
        altitude_anterior = altitude[i - 1] # IMPORTANTE GUARDAR ESSA USABILIDADE COMPARAR ITEM ANTERIOR COM O PROXIMO DA LISTA
        altitude_atual = altitude[i]

        queda = altitude_anterior - altitude_atual

        if queda > 500:
            turb_severa = True

        if queda > maior_queda:
            maior_queda = queda

    return turb_severa, maior_queda

turb_severa, maior_queda = turbulencia(altitude)

print(f"Houve turbulência severa? {turb_severa}")
print(f"Maior queda registrada: {maior_queda} metros")

