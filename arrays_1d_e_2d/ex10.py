# 10 - Um sistema acadêmico armazena as notas de 4 alunos em 3 avaliações através de
# uma matriz NumPy 4x3: (a) Dado a matriz de notas iniciais `notas = np.array([[5.0, 7.5,
# 6.0], [8.0, 9.0, 4.0], [3.5, 5.0, 6.5], [7.0, 6.0, 8.5]])`, calcule e exiba a média final de
# cada aluno; (b) Identifique qual avaliação (coluna) obteve a maior média geral da turma
# usando `np.argmax()`; (c) Aplique um reajuste automático atribuindo a nota mínima
# `6.0` a todas as avaliações com nota inferior a 6.0; (d) Remova a última coluna
# (Avaliação 3) da matriz utilizando `np.delete(..., axis=1)`.
import numpy as np

notas = np.array([[5.0, 7.5, 6.0], [8.0, 9.0, 4.0], [3.5, 5.0, 6.5], [7.0, 6.0, 8.5]])

for i in range(4):
    for j in range(3):
        print(notas[i][j], end=" ")
    print()

for i in range(len(notas)):
    media = sum(notas[i]) / len(notas[i])
    print(f"A media do aluno {i + 1} é de: {media:.2f}")

medias_coluna = np.mean(notas, axis=0)
melhor = np.argmax(medias_coluna)
print(f"amaior media da turma ocorreu na avaliaçao {melhor + 1} com: {medias_coluna[melhor]:.2f} de média geral.")

notas[notas < 6.0] = 6.0

for i in range(4):
    for j in range(3):
        print(notas[i][j], end=" ")
    print()

notas = np.delete(notas, 2, axis=1)
print()
for i in range(4):
    for j in range(2):
        print(notas[i][j], end=" ")
    print()