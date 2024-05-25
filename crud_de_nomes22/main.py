#crud = sistemas que fazem 4 operações -> cadastrar...
'''
crie um programa que tenha as opções:
    - cadastrar(inserir) pessoa na lista
    - listar pessoas cadastradas
    - pesquisar pelo nome de uma pessoa
    - ordenar a lista por ordem alfabética
    - atualizar nome
    - deletar nome da lista
    - sair do programa
'''

lista_de_pessoas = []

nome = input("Insira o nome:")

lista_de_pessoas.append(nome)

for pessoa in lista_de_pessoas:
    print(pessoa)

print("O que você deseja fazer?")
print("Deletar o nome de uma pessoa: digite 1")
print("Pesquisar o nome de uma pessoa: digite 2")
print("Ordenar a lista por ordem alfabetica: digite 3")
print("Atualizar o nome de uma pessoa: digite 4")
print("Sair do programa: digite 5")
