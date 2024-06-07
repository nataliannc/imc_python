#lista

nomes = ["Alex", "Simone", "Bernardo", "César", "Alexandra"]

#exibe a lista na tela
print(nomes)

#exime o primeiro elemento da lista
print(nomes[0]) 

#foi declarada a variavel 'nome' para os elementos da lista 'nomes'. 
for nome in nomes:
    print(nome)

#range = função para informar quantas vezes o laço for vai ser executado
for i in range(3): #foi declarada a variavel i, 3 exibe os 3 primeiros elementos da lista
    print(nomes[i])

#quando não se sabe quantos elemento se tem na lista
#len é uma função para medir o tamanho da variavel quando não se sabe o tamanho dela
for i in range(len(nomes)):
    print(nomes[i])

for i in range(len(nomes)):
    print(f'{i + 1}º nome da lista: {nomes[i]}.')

#ordana a lista em ordem alfabetica / sort = organizar
nomes.sort()

for nome in nomes:
    print(nome)

#ordana a lista em ordem reversa
nomes.sort(reverse=True)

for nome in nomes:
    print(nome)