nome = input("Qual é o seu nome?\n")
idade = int(input("Qual é a dua idade?\n"))
altura = str(input("Qual é a sua altura?\n")).replace(",","." #converte virgula para ponto

#converte altura para float
altura = float(altura)

#verifica as condições

if idade >= 12 and altura >= 1.20:
    print(f"{nome} pode entrar no brinquedo.")
else:
    print(f"{nome} não pode entrar no brinquedo.")