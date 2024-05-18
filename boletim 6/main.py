#entrada de dados
nome = input("Qual é o seu nome?")
nota = str(input("Qual é a sua nota?")).replace(",",".")

#converte nota para float
nota = float(nota)

#verifica a nota
if nota >= 7:
    print(f"{nome} está aprovado(a).")
elif nota >= 5: #se não se
    print(f"{nome} está de recuperação(a).")
else:
    print(f"{nome} está reprovado.(a)")



