#deletar itens de um alista

#lista
cidades = ["Brasília", "Taguatinga", "Gama", "Sobradinho"]

#usuário informa o nome que deseja deletar
cidade_deletada = input("Nome da cidade a ser deletada:")

#deleta a cidade informada
try:
    cidades.remove(cidade_deletada)
except:
    print("Não foi possível remover a cidade.")

#exibe a lista na tela
for cidade in cidades:
    print(cidade)