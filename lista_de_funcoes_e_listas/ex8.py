# 8 - Apuração de Urna Eletrônica: Recebemos uma lista gigantesca embaralhada
# contendo os IDs dos candidatos que receberam votos. O voto em branco é o ID 0. O
# sistema não sabe previamente quais são os IDs válidos.
# Retorno exigido: Uma estrutura em formato de lista de listas (ex: [[id,
# total_votos], ...]) resumindo a eleição, o ID do candidato vencedor e a
# porcentagem de votos em branco

votos = [0, 10, 0, 10, 30, 30, 30, 20, 0, 10, 10, 10, 0, 10, 10, 10, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 0, 0, 0, 10, 20, 30, 20, 30, 20, 20, 20]



def urna(votos):
    contagem = {}

    for voto in votos:
        if voto in contagem:
            contagem[voto] += 1
        else:
            contagem[voto] = 1
    candidatos = []
    for candidato in contagem:
        candidatos.append(candidato)
        resultado = []
        IDs = None
        mais_votado = 0
    for i in range(len(candidatos)):
        
       
        resultado.append([candidatos[i], contagem[candidatos[i]]])
        if contagem[candidatos[i]] > mais_votado:
            mais_votado = contagem[candidatos[i]]
            IDs = candidatos[i]
        Vbranco = contagem.get(0, 0) #importante também (revisar mais vezes)
        total_votos = sum(contagem.values()) # iimportante ter conhecimento disso
        branco = (Vbranco / total_votos) * 100


    print(f"O candidato vencedor é o ID: {IDs} com {mais_votado} votos, o percentual de votos em branco é de {branco:.2f}%")
    



urna(votos)
