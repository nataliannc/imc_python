def exibir_msg():
    print('-'*10,'BEM VINDO AO SENAI', '-'*10)
    print('Você está fazendo o CURSO DESENVOLVEDOR PYTHON!')

# programa principal
decisao = input('Gostaria de exibir a mensagem? "sim" para exibir ou "não" para não exibir')

match decisao:
    case 'sim':
        exibir_msg()
    case 'não':
        pass
    case _:
        print('Resposta inválida!')