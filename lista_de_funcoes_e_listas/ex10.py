# 10 - Decodificador de Sinais de Satélite: Um satélite envia pacotes de dados como uma
# lista de bits (0s e 1s). Um pacote de informação válido é sempre sinalizado pelo padrão
# exato de um 1 seguido imediatamente por dois 0s.
# Retorno exigido: O número total de pacotes válidos detectados e uma lista de
# índices marcando onde cada pacote válido começa.

bits = [1, 0, 0, 0, 0, 1, 0, 0, 1]

def decodificador(bits):
  pacote_valido = 0
  indices = []
  for i in range(len(bits) -2):
    if (bits[i] == 1) and (bits[i + 1] == 0) and (bits[i + 2] == 0):
      pacote_valido += 1
      indices.append(i)
  return pacote_valido, indices
 

total, indices = decodificador(bits)

print(f"Total de pacotes válidos : {total}. Indíces que iniciam os respectivos pacotes válidos: {indices}")