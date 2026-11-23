# 6 - Faça um programa que apresente o seguinte menu de opções:
# 1. Criar
# 2. Incluir
# 3. Sair
# Digite a opção desejada
# Na opcão 1: criar um arquivo com os campos: numero, nome, nota1 e nota2.
# Na opção 2: incluir todos os dados digitados, podendo haver repetição. No final
# da inclusão após pressionar ENTER o programa deve mostrar todos os registros
# cadastrado

import pandas as pd

arquivo = "alunos.csv"
colunas = ["numero", "nome", "nota1", "nota2"]

while True:
    print("\n1. Criar")
    print("2. Incluir")
    print("3. Sair")
    opcao = input("Digite a opção desejada: ").strip()

    if opcao == "1":
        pd.DataFrame(columns=colunas).to_csv(arquivo, index=False)
        print("Arquivo criado com sucesso!")

    elif opcao == "2":
        try:
            alunos = pd.read_csv(arquivo, dtype=str)
        except FileNotFoundError:
            print("Crie o arquivo primeiro (opção 1).")
            continue

        while True:
            numero = input("Número (ENTER para encerrar a inclusão): ").strip()
            if numero == "":
                break

            nome = input("Nome: ").strip()

            try:
                nota1 = float(input("Nota 1: ").replace(",", "."))
                nota2 = float(input("Nota 2: ").replace(",", "."))
            except ValueError:
                print("Nota inválida. Registro não incluído.")
                continue

            novo = pd.DataFrame([[numero, nome, f"{nota1:.1f}", f"{nota2:.1f}"]], columns=colunas)
            alunos = pd.concat([alunos, novo], ignore_index=True)

        alunos.to_csv(arquivo, index=False)

        print("\n===== REGISTROS CADASTRADOS =====")
        if alunos.empty:
            print("Nenhum registro cadastrado.")
        else:
            print(alunos.to_string(index=False))

    elif opcao == "3":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")