# 2 - Faça um programa para cadastrar clientes no arquivo criado no Exercício 1.

import pandas as pd

arquivo = "clientes.csv"
continuar = "s"

while continuar == "s":
    clientes = pd.read_csv(arquivo, dtype=str)

    cod = input("Código do cliente: ").strip()
    nome = input("Nome: ").strip()
    endereco = input("Endereço: ").strip()
    fone = input("Telefone: ").strip()

    if cod == "" or nome == "":
        print("Código e nome são obrigatórios.")
    elif cod in clientes["Cod_Cli"].values:
        print("Já existe um cliente com esse código.")
    else:
        novo = pd.DataFrame([[cod, nome, endereco, fone]], columns=clientes.columns)
        clientes = pd.concat([clientes, novo], ignore_index=True)
        clientes.to_csv(arquivo, index=False)
        print("Cliente cadastrado com sucesso!")

    continuar = input("Cadastrar outro? (s/n): ").strip().lower()