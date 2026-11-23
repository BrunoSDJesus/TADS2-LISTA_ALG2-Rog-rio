# 9 - Desenvolva um programa completo em Python nativo para controle de estoque de
# uma empresa. Utilize duas listas paralelas: `produtos` (strings) e `quantidades`
# (inteiros). Implemente um menu interativo dentro de um laço `while` com as opções: 1.
# Cadastrar Produto; 2. Listar Estoque; 3. Atualizar Quantidade; 4. Excluir Produto; 5.
# Sair. Garantir a integridade dos índices sincronizados entre as duas listas

produtos = []
quantidades = []

while True:
    print("\n===== CONTROLE DE ESTOQUE =====")
    print("1. Cadastrar Produto")
    print("2. Listar Estoque")
    print("3. Atualizar Quantidade")
    print("4. Excluir Produto")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        nome = input("Nome do produto: ").strip()

        if nome == "":
            print("O nome do produto não pode ficar vazio.")
            continue

        if nome.lower() in [p.lower() for p in produtos]:
            print("Esse produto já está cadastrado.")
            continue

        try:
            quantidade = int(input("Quantidade inicial: "))

            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
                continue

            produtos.append(nome)
            quantidades.append(quantidade)

            print("Produto cadastrado com sucesso!")

        except ValueError:
            print("Digite uma quantidade inteira válida.")

    elif opcao == "2":
        if len(produtos) == 0:
            print("O estoque está vazio.")
        else:
            print("\n===== ESTOQUE ATUAL =====")

            for i in range(len(produtos)):
                print(f"ID: {i} | Produto: {produtos[i]} | Quantidade: {quantidades[i]}")

    elif opcao == "3":
        if len(produtos) == 0:
            print("Não há produtos cadastrados.")
            continue

        for i in range(len(produtos)):
            print(f"ID: {i} | Produto: {produtos[i]} | Quantidade: {quantidades[i]}")

        try:
            id_produto = int(input("Digite o ID do produto: "))

            if id_produto < 0 or id_produto >= len(produtos):
                print("ID inválido.")
                continue

            nova_quantidade = int(input("Digite a nova quantidade: "))

            if nova_quantidade < 0:
                print("A quantidade não pode ser negativa.")
                continue

            quantidades[id_produto] = nova_quantidade

            print("Quantidade atualizada com sucesso!")

        except ValueError:
            print("Digite um número inteiro válido.")

    elif opcao == "4":
        if len(produtos) == 0:
            print("Não há produtos para excluir.")
            continue

        for i in range(len(produtos)):
            print(f"ID: {i} | Produto: {produtos[i]} | Quantidade: {quantidades[i]}")

        try:
            id_produto = int(input("Digite o ID do produto que deseja excluir: "))

            if id_produto < 0 or id_produto >= len(produtos):
                print("ID inválido.")
                continue

            produto_removido = produtos.pop(id_produto)
            quantidades.pop(id_produto)

            print(f"Produto '{produto_removido}' excluído com sucesso!")

        except ValueError:
            print("Digite um ID inteiro válido.")

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
