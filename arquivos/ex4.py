# 4 - Faça um programa que exclua clientes e, consequentemente, todos os seus
# recebimentos, do arquivo criado no Exercício l.

import pandas as pd

arq_cli = "clientes.csv"
arq_rec = "recebimentos.csv"
continuar = "s"

while continuar == "s":
    clientes = pd.read_csv(arq_cli, dtype=str)
    receb = pd.read_csv(arq_rec, dtype=str)

    cod = input("Código do cliente a excluir: ").strip()

    if cod not in clientes["Cod_Cli"].values:
        print("Cliente não encontrado.")
    else:
        nome = clientes.loc[clientes["Cod_Cli"] == cod, "Nome"].values[0]
        qtd = (receb["Cod_Cli"] == cod).sum()

        print(f"Cliente: {nome} | Recebimentos vinculados: {qtd}")
        confirma = input("Confirma a exclusão do cliente e de todos os seus recebimentos? (s/n): ").strip().lower()

        if confirma == "s":
            clientes = clientes[clientes["Cod_Cli"] != cod]
            receb = receb[receb["Cod_Cli"] != cod]

            clientes.to_csv(arq_cli, index=False)
            receb.to_csv(arq_rec, index=False)

            print(f"Cliente '{nome}' e {qtd} recebimento(s) excluídos com sucesso!")
        else:
            print("Exclusão cancelada.")

    continuar = input("Excluir outro? (s/n): ").strip().lower()