#tupla
chaves = ("Nome", "Idade", "E-mail", "Profissão")

#lista de dicionários
pessoas = [
    {
        chaves[0]: "Alex Machado",
        chaves[1]: 39,
        chaves[2]: "alex@gmail.com",
        chaves[3]: "Programador"
    },
    {
        chaves[0]: "Ana Julia",
        chaves[1]: 50,
        chaves[2]: "ana@gmail.com",
        chaves[3]: "Dentista"
    },
    {
        chaves[0]: "Pablo",
        chaves[1]: 18,
        chaves[2]: "escobar@gmail.com",
        chaves[3]: "Vendedor"
    }
]

#exibe a lista
for pessoa in pessoas:
    for chave in pessoa:
        print(f"{chave}:{pessoa.get(chave)}")


# campos = ("Nome", "CPF", "Telefone")
# cadastros = []

# cadastro[cadastro[0]]
# cadastro[cadastro[1]]
# cadastro[cadastro[2]]