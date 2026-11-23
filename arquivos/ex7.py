# 7 - Gerenciador CRUD de Produtos
# Desenvolva um sistema de controle de estoque em Python nativo que armazene
# registros de produtos em um arquivo estruturado ‘produtos.csv’, contendo os campos:
# • codigo,
# • descricao
# • preco.
# a) O programa deve apresentar um menu interativo permitindo realizar todas as
# operações do ciclo de vida dos dados no arquivo.
# b) Antes de inserir um novo produto, abra o arquivo em modo leitura e percorra os
# registros para buscar se o ‘codigo’ informado já existe. Se não existir, abra o
# Instituto Federal de Mato Grosso do Sul
# Lista de Exercícios
# arquivo no modo anexo e adicione o novo registro ao final sem apagar os
# dados anteriores.
# c) O programa também deve permitir a procura, atualização e remoção de um
# registro.

import csv
import os

arquivo = "produtos.csv"
cabecalho = ["codigo", "descricao", "preco"]


def garantir_arquivo():
    if not os.path.exists(arquivo):
        with open(arquivo, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(cabecalho)


def ler_todos():
    with open(arquivo, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def gravar_todos(registros):
    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=cabecalho)
        escritor.writeheader()
        escritor.writerows(registros)


def codigo_existe(codigo):
    with open(arquivo, "r", newline="", encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            if linha["codigo"] == codigo:
                return True
    return False


def ler_preco(mensagem):
    try:
        preco = float(input(mensagem).replace(",", "."))
    except ValueError:
        return None
    if preco < 0:
        return None
    return preco


garantir_arquivo()

while True:
    print("\n===== GERENCIADOR DE PRODUTOS =====")
    print("1. Inserir")
    print("2. Listar")
    print("3. Procurar")
    print("4. Atualizar")
    print("5. Remover")
    print("6. Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        codigo = input("Código: ").strip()
        if codigo == "":
            print("O código é obrigatório.")
        elif codigo_existe(codigo):
            print("Já existe um produto com esse código.")
        else:
            descricao = input("Descrição: ").strip()
            preco = ler_preco("Preço: ")
            if descricao == "" or preco is None:
                print("Descrição vazia ou preço inválido. Produto não cadastrado.")
            else:
                with open(arquivo, "a", newline="", encoding="utf-8") as f:
                    csv.writer(f).writerow([codigo, descricao, f"{preco:.2f}"])
                print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        registros = ler_todos()
        if len(registros) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for r in registros:
                print(f"Código: {r['codigo']} | {r['descricao']} | R$ {r['preco']}")

    elif opcao == "3":
        codigo = input("Código a procurar: ").strip()
        achou = False
        for r in ler_todos():
            if r["codigo"] == codigo:
                print(f"Código: {r['codigo']} | {r['descricao']} | R$ {r['preco']}")
                achou = True
                break
        if not achou:
            print("Produto não encontrado.")

    elif opcao == "4":
        codigo = input("Código do produto a atualizar: ").strip()
        registros = ler_todos()
        achou = False
        for r in registros:
            if r["codigo"] == codigo:
                achou = True
                print(f"Atual: {r['descricao']} | R$ {r['preco']}")
                print("Deixe em branco (ENTER) para manter o valor atual.")
                nova_desc = input("Nova descrição: ").strip()
                novo_preco = input("Novo preço: ").strip()
                if nova_desc != "":
                    r["descricao"] = nova_desc
                if novo_preco != "":
                    try:
                        valor = float(novo_preco.replace(",", "."))
                        if valor < 0:
                            print("Preço negativo ignorado.")
                        else:
                            r["preco"] = f"{valor:.2f}"
                    except ValueError:
                        print("Preço inválido ignorado.")
                gravar_todos(registros)
                print("Produto atualizado!")
                break
        if not achou:
            print("Produto não encontrado.")

    elif opcao == "5":
        codigo = input("Código do produto a remover: ").strip()
        registros = ler_todos()
        restantes = [r for r in registros if r["codigo"] != codigo]
        if len(restantes) == len(registros):
            print("Produto não encontrado.")
        else:
            confirma = input("Confirma a remoção? (s/n): ").strip().lower()
            if confirma == "s":
                gravar_todos(restantes)
                print("Produto removido com sucesso!")
            else:
                print("Remoção cancelada.")

    elif opcao == "6":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")