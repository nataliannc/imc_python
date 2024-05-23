nome = input("Qual é o seu nome?")
idade = int(input("Qual é a sua idade?"))

while True:

    filme1 = "Sala 1 - Procurando o Nemo. Classifiação indicativa: Livre"
    filme2 = "Sala 2 - Pikachu. Classifiação indicativa: Livre"
    filme3 = "Sala 3 - Senhor dos Aneis. Classifiação indicativa: Livre"
    filme4 = "Sala 4 - Star Wars. Classifiação indicativa: +10 anos"
    filme5 = "Sala 5 - O Pianista. Classifiação indicativa: +12 anos"

    print("LISTA DE FILMES\n")
    print(filme1)
    print(filme2)
    print(filme3)
    print(filme4)
    print(filme5)

    sala = int(input("informe a sala desejada:"))

    if sala == 1 and idade >=0:
        print(f"Filme escolhido por {nome}: {filme1} Divirta-se!")
    elif sala == 2 and idade >=0:
        print(f"Filme escolhido por {nome}: {filme2} Divirta-se!")
    elif sala == 3 and idade >=0:
        print(f"Filme escolhido por {nome}: {filme3} Divirta-se!")
    elif sala == 4 and idade >=10:
        print(f"Filme escolhido por {nome}: {filme4} Divirta-se!")
    elif sala == 5 and idade >=12:
        print(f"Filme escolhido por {nome}: {filme5} Divirta-se!")
    else:
        print("Você não pode assistir este filme. Escolha outro filme.")

    continuar = input("Deseja escolher outro filme (s/n)?")

    if continuar == "s":
        continue
    elif continuar == "n":
        break
    else:
        print("Opção inválida")
        continue