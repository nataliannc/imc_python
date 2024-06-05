#deletar itens de um alista

#lista
cidades = ["Brasília", "Taguatinga", "Gama", "Sobradinho"]

#informa a posição do item a ser deletado
indice = int(input("Informe a posição do item a ser deletado:"))

#evita que o usuário apague um item da lista caso indice=0
if indice > 0:
    indice -= 1
else:
    indice = ''

#deleta item da lista
try:
    del(cidades[indice])
except:
    print("Não foi possível deletar.")

#exibe a lista 
for cidade in cidades:
    print(cidade)