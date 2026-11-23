# 2 - Dada a lista estática de salários `salarios = [2500.0, 3200.0, 1800.0, 4500.0,
# 2100.0]`: (a) Atualize o salário no índice 2 para 2300.0; (b) Peça ao usuário um valor de
# salário para buscar e verificar se existe na lista usando o operador `in`; (c) Se existir,
# remova-o usando `.remove()`; (d) Extraia e remova o último elemento da lista utilizando
# `.pop()` e exiba o elemento removido.

salarios = [2500.0, 3200.0, 1800.0, 4500.0, 2100.0]

salarios[2] = 2300.0

print(salarios)

n = float(input("Insira um valor de salario: "))

if n in salarios:
    print(f"o salario {n} existe na lista salarios.")
    salarios.remove(n)
    ultimo_elemento = len(salarios) - 1
    print(f' removendo o ultimo salario : {salarios[ultimo_elemento]}')
    salarios.pop(ultimo_elemento)
    print(salarios)
else:
    print(f"O salario {n} não existe na lista salarios!. ")
