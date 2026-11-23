# 2 - Um serviço de streaming tem seu catálogo representado por uma lista de tuplas
# (titulo_filme, ano_lancamento, genero, avaliacao_usuarios). Você também receberá
# como parâmetro um genero_alvo (string) e uma nota_corte (float).
# Você deve extrair dados com base em múltiplos parâmetros de entrada e encontrar o
# "menor valor" (mais antigo) dentro de um subconjunto específico.
# Retorno Exigido: Uma lista apenas com os títulos dos filmes que batem com o gênero
# alvo e possuem nota igual ou superior ao corte, e uma tupla com o (titulo_filme,
# ano_lancamento) do filme mais antigo dessa lista filtrada.
# Na Main: Construa uma lista estática com pelo menos 4 filmes misturando gêneros e
# notas. Defina variáveis para o seu gênero alvo e sua nota de corte. Invoque a função e
# imprima a lista final de filmes aprovados, seguida de uma mensagem informando qual é
# o filme mais antigo dentre os que foram filtrados


def main():
    nota_corte = 7.0
    genero = "Ação"

    filmes = [
        ("Homem-Aranha", 2002, "Ação", 8.5),
        ("Vingadores", 2012, "Ação", 9.0),
        ("Bad Boys", 1995, "Comédia", 7.5),
        ("Fuga das Galinhas", 2000, "Animação", 8.0)
    ]

    filmes_aprovados, filme_mais_antigo = catalogo(
        filmes, nota_corte, genero
    )

    print("Filmes aprovados:", filmes_aprovados)

    if filme_mais_antigo is not None:
        print(
            f"Filme mais antigo: {filme_mais_antigo[0]}, "
            f"lançado em {filme_mais_antigo[1]}"
        )
    else:
        print("Nenhum filme foi aprovado.")


def catalogo(filmes, nota_corte, genero):
    nome = []
    ano_lancamento = None
    titulo_filme = None

    for i in range(len(filmes)):
        if filmes[i][2] == genero and filmes[i][3] >= nota_corte:

            nome.append(filmes[i][0])

            if ano_lancamento is None or filmes[i][1] < ano_lancamento:
                titulo_filme = filmes[i][0]
                ano_lancamento = filmes[i][1]

    if titulo_filme is None:
        filme = None
    else:
        filme = (titulo_filme, ano_lancamento)

    return nome, filme


main()
