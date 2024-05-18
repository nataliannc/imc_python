# declaração de variáveis

nome = 'Natália' #string
idade = 28 #int
altura = 1.63 #ponto flutuante = float
programador = False #booleano (iniciar com letra maiúscula

#saída de dados
#usa-se str() para transformar uma variável int em string

print ('Meu nome é: ' + nome + '.')
print ('Eu tenho ' + str(idade) + '.') 

print ('Nome: {}.' .format(nome))
print ('Idade: {}.' .format(idade))
print ('Meu nome é {} e tenho {} anos.' .format(nome, idade))

print (f'Meu nome é: {nome} e tenho {idade} anos.')

#retornar o tipo da variável
print(type(nome))
print(type(idade))
print(type(altura))
print(type(programador))

