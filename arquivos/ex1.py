# 1 - Faça um programa para criar os arquivos a seguir:
# Clientes: Cod_Cli, Nome, Endereco, Fone
# Recebimentos: Num_doc, Valor_doc, Data_Emissao, Data_Vencimento, Cod_Cli.

import pandas as pd

clientes = pd.DataFrame(columns=["Cod_Cli", "Nome", "Endereco", "Fone"])
recebimentos = pd.DataFrame(columns=["Num_doc", "Valor_doc", "Data_Emissao", "Data_Vencimento", "Cod_Cli"])

clientes.to_csv("clientes.csv", index=False)
recebimentos.to_csv("recebimentos.csv", index=False)

print("Arquivos criados com sucesso!")