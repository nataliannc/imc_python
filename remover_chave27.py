pessoa = {
    "Nome" : "Alex",
    "Idade" : 39,
    "Profissão" : "Programador",
    "Empresa": "Senai",
    "Gênero": "Masculino",
    "Cidade": "Taguatinga"
}

#remover chave

del pessoa[input("Informe o nome da chave a ser deletada:")]
           
for chave in pessoa:
    print(f"{chave}: {pessoa.get(chave)}")
