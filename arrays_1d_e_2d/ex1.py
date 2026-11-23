# 1 - Escreva um programa em Python que solicite ao usuário a quantidade N de números
# inteiros que deseja cadastrar. Construa uma lista vazia e preencha-a dinamicamente em
# tempo de execução utilizando o método append(). Em seguida, percorra a lista e exiba:
# (a) o maior e o menor valor digitados; (b) a média aritmética dos elementos; e (c) a
# quantidade de números pares

def cadastro(num):
    numeros = []
    maior = None
    menor = None
    par = 0

    for _ in range(num):
        n = int(input("Insira o numero: "))
        numeros.append(n)

        if maior is None or n > maior:
            maior = n

        if menor is None or n < menor:
            menor = n

        if n % 2 == 0:
            par += 1

    media = sum(numeros) / len(numeros)

    print(f"maior e menor: {maior}, {menor}")
    print(f"média aritmetica: {media}")
    print(f"quantidade de numeros pares: {par}")


num = int(input("Insira aa quantidade de numeros que deseja cadastrar: "))
cadastro(num)