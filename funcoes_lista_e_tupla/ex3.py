# 3 - O sistema do caixa gera um recibo na forma de uma lista de tuplas (codigo_produto,
# quantidade, preco_unitario).
# Você deve multiplicar valores internos da tupla para criar dados novos (valor total do
# item), acumular um montante geral e guardar o registro do maior valor calculado.
# Retorno Exigido: O valor total da compra e uma tupla (codigo_produto,
# valor_total_do_item) representando exclusivamente o item que teve o maior custo
# absoluto na nota fiscal.
# Na Main: Monte uma lista de tuplas representando o "carrinho" de um cliente com 3 ou
# mais itens diferentes. Execute a função recebendo os retornos e imprima no terminal o
# valor total da nota fiscal (formatado com R$ e duas casas decimais) e os detalhes do
# produto que saiu mais caro na conta final.

def main():
    carrinho = [
        (1, 4, 12),
        (2, 2, 50),
        (3, 22, 7.55)
    ]
    valor_total_compra, item_mais_caro = caixa(carrinho)

    print(f"Total da nota fiscal: R$ {valor_total_compra:.2f}")
    print(f"Produto mais caro: código {item_mais_caro[0]}")
    print(f"Valor do item: R$ {item_mais_caro[1]:.2f}")


def caixa(carrinho):
    itens_valores = []
    valor_item = 0
    maior_valor = None
    valor_total_compra = 0
    maior_item = 0

    for i in range(len(carrinho)):
        valor_item = (carrinho[i][1] * carrinho[i][2])
        itens_valores.append(valor_item)
        valor_total_compra += valor_item

        if (maior_valor == None or maior_valor < valor_item):
            maior_item = carrinho[i][0]
            maior_valor = valor_item
    return valor_total_compra, (maior_item, maior_valor)

main()