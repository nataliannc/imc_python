#lista de 15 nomes
nomes = ["João", "Bethoven", "Francisco", "Jose", "Bento", "Ana", "Julia", "Beatriz", "Amanda", "Jackson", "Roberto", "Caio", "Vitor", "Mauricio", "Cris"]

#usuario informa o nome que deseja pesquisar

#capitalize() -> transforma a primeira letra digitada pelo usuário em maiuscula
nome = input("Digite o nome a ser pesquisado:").capitalize()

#retorna o nome da posição do indice
#nome = nomes[indice]
 
#verifica se o nome está na lista ou não
try:
    #retorna o indice do nome pesquisado
    indice = nomes.index(nome)
    print(f"{nome} encontrado(a) no índice {indice}.")
except:
    print(f"{nome} não encontrado na lista.")