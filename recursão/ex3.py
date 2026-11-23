# Exercício 3: Contagem Regressiva

# Crie uma função recursiva que receba um número inteiro N e imprima a contagem regressiva de N até 1.

def contagem(n):
    if n < 1:
        return
    print(n)
    contagem(n - 1)

contagem(4)       