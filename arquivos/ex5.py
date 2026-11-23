# 5 - Faça um programa que altere o cadastro de clientes do Exercício 1. O usuário deve
# informar o código do cliente que será alterado.

import pandas as pd

arq_cli = "clientes.csv"
continuar = "s"

while continuar == "s":
    clientes = pd.read_csv(arq_cli, dtype=str).fillna("")

    cod = input("Código do cliente a alterar: ").strip()

    if cod not in clientes["Cod_Cli"].values:
        print("Cliente não encontrado.")
    else:
        pos = clientes.index[clientes["Cod_Cli"] == cod][0]

        print(f"Nome atual: {clientes.loc[pos, 'Nome']}")
        print(f"Endereço atual: {clientes.loc[pos, 'Endereco']}")
        print(f"Telefone atual: {clientes.loc[pos, 'Fone']}")
        print("Deixe em branco (Enter) para manter o valor atual.")

        nome = input("Novo nome: ").strip()
        endereco = input("Novo endereço: ").strip()
        fone = input("Novo telefone: ").strip()

        if nome != "":
            clientes.loc[pos, "Nome"] = nome
        if endereco != "":
            clientes.loc[pos, "Endereco"] = endereco
        if fone != "":
            clientes.loc[pos, "Fone"] = fone

        clientes.to_csv(arq_cli, index=False)
        print("Cadastro alterado com sucesso!")

    continuar = input("Alterar outro? (s/n): ").strip().lower()