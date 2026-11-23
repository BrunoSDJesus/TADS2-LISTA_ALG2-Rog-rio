# Exercício 4: Algoritmo de Euclides (MDC)

# Implemente de forma recursiva o algoritmo de Euclides para calcular o Maior Divisor Comum (MDC) entre dois números inteiros positivos 'a' e 'b'.

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

print(mdc(48, 18))   