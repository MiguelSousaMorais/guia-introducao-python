#   Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#   No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = input("Digite o nome do aluno: ")
aluno['media'] = float(input("Digite a média do aluno: "))

print("Nome:", aluno['nome'])
print("Média:", aluno['media'])
print("Situação do aluno: O aluno tem média ", aluno['media'], " até então")