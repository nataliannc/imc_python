'''
Crie um programa onde o usuário cria uma lista de tarefas a ser executada no dia. 
Ao terminar, crie um repositorio local e suba para o repositório remoto no GitHub.
'''

#lista vazia
tarefas = []

while True:
    #usuário informa item da tarefa
    nova_tarefa = input("Insira uma tarefa na sua lista de tarefas ou deixe vazio para encerrar e exibir a lista:")

    #verifica se o usuário inseriu nova tarefa
    if nova_tarefa != '': #!= diferente
        tarefas.append(nova_tarefa)
        continue
    else:
        break

#exibe a lista de tarefas
for tarefa in tarefas:
    print(tarefa)