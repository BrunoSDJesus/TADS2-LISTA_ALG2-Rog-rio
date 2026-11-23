# 3 - Faça um programa que inclua recebimentos no arquivo criado no Exercício 1,
# devendo verificar se o cliente já se encontra cadastrado.

import pandas as pd

arq_cli = "clientes.csv"
arq_rec = "recebimentos.csv"
continuar = "s"

while continuar == "s":
    clientes = pd.read_csv(arq_cli, dtype=str)
    receb = pd.read_csv(arq_rec, dtype=str)

    cod = input("Código do cliente: ").strip()

    if cod not in clientes["Cod_Cli"].values:
        print("Cliente não cadastrado. Cadastre-o antes de incluir o recebimento.")
    else:
        num = input("Número do documento: ").strip()

        if num == "":
            print("O número do documento é obrigatório.")
        elif num in receb["Num_doc"].values:
            print("Já existe um recebimento com esse número de documento.")
        else:
            try:
                valor = float(input("Valor do documento: ").replace(",", "."))
                emissao = pd.to_datetime(input("Data de emissão (dd/mm/aaaa): "), format="%d/%m/%Y")
                venc = pd.to_datetime(input("Data de vencimento (dd/mm/aaaa): "), format="%d/%m/%Y")

                if valor <= 0:
                    print("O valor deve ser maior que zero.")
                elif venc < emissao:
                    print("O vencimento não pode ser anterior à emissão.")
                else:
                    novo = pd.DataFrame(
                        [[num, f"{valor:.2f}", emissao.strftime("%d/%m/%Y"), venc.strftime("%d/%m/%Y"), cod]],
                        columns=receb.columns,
                    )
                    receb = pd.concat([receb, novo], ignore_index=True)
                    receb.to_csv(arq_rec, index=False)
                    print("Recebimento incluído com sucesso!")

            except ValueError:
                print("Valor ou data inválidos. Use números no valor e o formato dd/mm/aaaa nas datas.")

    continuar = input("Incluir outro? (s/n): ").strip().lower()