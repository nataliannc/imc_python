tupla = ("Nome", "Idade", "Profissão")
lista = ["Nome", "Idade", "Profissão"]
dicionario = {"Nome", "Idade", "Profissão"}

#dicionário
pessoa = {
    "Nome" : "Alex",
    "Idade" : 39,
    "Profissão" : "Programador"
}

#exibe os dados na tela
print(pessoa)

print(f"Nome: {pessoa["Nome"]}")

#não é a melhor forma de exibir dados do dicionário
try: 
    print(pessoa["Cidade"])
except:
    ("Dado não encontrado")

#exibe os dados na tela
print(pessoa.get("Nome"))


for nome in pessoa:
    print(f"{nome}: {pessoa.get(nome)}")