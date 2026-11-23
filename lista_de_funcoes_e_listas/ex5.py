# 5 - Controle de Qualidade Agrícola: Uma fazenda colhe maçãs e as classifica pelo peso
# (em gramas). Você receberá a lista de pesos, o peso mínimo para exportação e o peso
# máximo.
# Retorno exigido: Uma lista contendo os pesos aprovados, uma segunda lista com
# os pesos descartados, e a porcentagem de perda da safra (número float).

pesos = [500, 400, 300, 200, 100, 150, 180, 270]
peso_min = 150
peso_max = 250
def controleQualidade():
    ap = []
    rp = []

    for fruta in pesos:
        if fruta >= 150 and fruta <= 250:
            ap.append(fruta)
        else: 
            rp.append(fruta)
    perda = ((len(rp))/(len(ap) + len(rp))) * 100
    print(f"a perda da safra foi de {perda}%")

controleQualidade()