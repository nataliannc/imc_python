# função que recebe o nome do usuário e envia uma mensagem personalizada
def exibir_msg(nome):
    print(f'{'-'*20} Olá {nome}, seja bem vindo ao SENAI {'-'*20}')

# programa principal
nome = input('Informe seu nome: ')

# chama a função
exibir_msg(nome)

# função que recebe o nome do usuário e do curso, e envia uma mensagem personali
def exibir_msg(nome, curso):
    print(f'Olá {nome}, seja bem vindo ao SENAI. Você está fazendo o curso {curso}.')

# programa principal
nome = input('Informe seu nome: ')
curso = input('Informe o nome do seu curso: ')

# chama a função
exibir_msg(nome, curso)