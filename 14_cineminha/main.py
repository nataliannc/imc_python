import os #traz os comamandos do sistema operacional para o python

nome = str(input("Qual é o seu nome?"))
idade = int(input("Qual é a sua idade?"))

os.system("cls") #limpa console

while True:

    filme1 = "Sala 1 - Procurando o Nemo. Classificação indicativa: Livre"
    filme2 = "Sala 2 - Pikachu. Classificação indicativa: Livre"
    filme3 = "Sala 3 - Senhor dos Aneis. Classificação indicativa: Livre"
    filme4 = "Sala 4 - Star Wars. Classificação indicativa: +10 anos"
    filme5 = "Sala 5 - O Pianista. Classificação indicativa: +12 anos"

    print(f"{"="*20} LISTA DE FILMES {"="*20}\n") #{"="*20} -> mostra o sinal de = 20 vezes seguidas
    print(filme1)
    print(filme2)
    print(filme3)
    print(filme4)
    print(filme5)

    sala = int(input("Informe a sala desejada:"))

    os.system("cls")

    if sala == 1 and idade >=0:
        print(f"Filme escolhido por {nome}:\n {filme1}. Divirta-se!")
    elif sala == 2 and idade >=0:
        print(f"Filme escolhido por {nome}:\n {filme2}. Divirta-se!")
    elif sala == 3 and idade >=0:
        print(f"Filme escolhido por {nome}:\n {filme3}. Divirta-se!")
    elif sala == 4 and idade >=10:
        print(f"Filme escolhido por {nome}:\n {filme4}. Divirta-se!")
    elif sala == 5 and idade >=12:
        print(f"Filme escolhido por {nome}:\n {filme5}. Divirta-se!")
    else:
        print("Você não pode assistir este filme.")

    continuar = input("Deseja escolher um filme apropriado para a sua idade (s/n)?")

    if continuar == "s":
        continue
    elif continuar == "n":
        break
    else:
        print("Opção inválida")
        continue