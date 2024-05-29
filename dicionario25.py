"""
Crie um dicionário em Python com os seguintes dados de uma pessoa:
- Nome
- CPF
- RG
- Data de Nascimento
- Gênero
- E-mail
- Telefone
- Tipo sanguíneo
- Profissão
- Empresa

O usuário deverá informar os dados da pessoa.
O programa deverá exibir os dados da pessoa no console.
"""

pessoa = {
    "Nome": input("Informe o nome:"),
    "CPF": input("Informe o CPF:"),
    "RG": input("Informe o RG:"),
    "Data de Nascimento": input("Informe a data de nascimento:"),
    "Gênero": input("Informe o gênero:"),
    "E-mail": input("Informe o gênero:"),
    "Telefone": input("Informe o telefone:"),
    "Tipo sanguíneo": input("Informe o tipo sanguíneo:"),
    "Profissão": input("Informe a profissão:"),
    "Empresa": input("Informe a empresa:")
}

for chave in pessoa:
    print(f"{chave}: {pessoa.get(chave)}")
