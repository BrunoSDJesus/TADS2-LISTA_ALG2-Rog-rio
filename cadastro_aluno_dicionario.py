# Crie um sistema de cadastro de alunos utilizando dicionários em Python. Para cada aluno, o sistema deverá armazenar seu nome e quatro notas.

# O sistema deverá apresentar um menu de opções para que o usuário possa realizar as seguintes operações:

# -Adicionar um aluno: permitir que o usuário cadastre um novo aluno, informando seu nome e suas quatro notas.
# -Remover um aluno: permitir que o usuário escolha e remova um aluno já cadastrado.
# -Calcular a média de todos os alunos: exibir a média das notas de cada aluno cadastrado.
# -Identificar o aluno com a maior média: informar o nome do aluno que possui a maior média.
# -Exibir todos os alunos: imprimir o nome, as quatro notas e a média de cada aluno cadastrado.
# -Sair do sistema: disponibilizar uma opção para encerrar a execução do programa.

# O programa deverá continuar apresentando o menu e permitindo novas operações até que o usuário escolha a opção de sair.

alunos = []

def adicionarAluno(alunos):
 
    nome = input("Insira o nome do aluno: ")

    notas = []
   
    for i in range(4):
        nota = float(input(f"Insira a nota {i + 1}:  "))
        notas.append(nota)

    aluno = {
        "nome": nome,
        "notas": notas
        }

    alunos.append(aluno)

def removerAluno(alunos):
    
    if not alunos:
        print("Ainda não há alunos matriculados! ")
        return

    print("Alunos inscritos: ")
    for i, aluno in enumerate(alunos):
        print(f"ID aluno: {i} Nome: {aluno['nome']}")
    num = int(input("Insira o id do aluno que deseja excluir: "))
    alunos.pop(num)

    print("Alunos remanescentes: ")
    for i, aluno in enumerate(alunos):
            print(f"ID aluno: {i} Nome: {aluno['nome']}")

def calcularMediaAlunos(alunos):
    if not alunos:
        print("Ainda não há alunos matriculados! ")
        return
    
    for aluno in alunos:
        mediaalunos = ((sum(aluno["notas"])) / len(aluno["notas"]))
        print(f"A média do aluno {aluno['nome']} é: {mediaalunos} ")
        
def identificarAluno(alunos):
    if not alunos:
            print("Ainda não há alunos matriculados! ")
            return

    melhor_aluno = alunos[0]
    maior_media = sum(alunos[0]['notas']) / len(alunos[0]["notas"])
    for aluno in alunos:
        mediaalunos = ((sum(aluno["notas"])) / len(aluno["notas"]))
        media_atual = mediaalunos
        if media_atual > maior_media:
             maior_media = media_atual
             melhor_aluno = aluno

    print(f"O aluno com a maior média é o {melhor_aluno["nome"]} com a média de {maior_media}")


def exibirTodosAlunos(alunos):
    if not alunos:
        print("Ainda não há alunos matriculados! ")
        return

    print("Todos os alunos matriculados: ")
    print("-----------------------------")
    for aluno in alunos:
        print(f"Estudante {aluno['nome'], {aluno['notas']}}")


while True:

    print("\nEscolha dentre as seguintes opções:" \
    "\n1- Adicionar Aluno" \
    "\n2- Remover Aluno" \
    "\n3- Calcular a média de todos os alunos" \
    "\n4- Identificar aluno com maior média" \
    "\n5- Exibir todos os alunos" \
    "\n6- Sair do sistema\n" \
    "")

    opcao = int(input("\n Qual opção deseja ? "))
    if(opcao == 6):
        print("\nEntendido !")
        print("Fechando sistema........ ")
        print(".........")
        print(". . .")
        break
    elif(opcao == 1):
        print("\n")
        adicionarAluno(alunos)
    elif(opcao == 2):
        print("\n")
        removerAluno(alunos)
    elif(opcao == 3):
        print("\n")
        calcularMediaAlunos(alunos)
    elif(opcao == 4):
        print("\n")
        identificarAluno(alunos)
    elif(opcao == 5):
        exibirTodosAlunos(alunos)
