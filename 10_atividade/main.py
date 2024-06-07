"""
caulcule a nota do boletim
"""

nota1 = str(input("Qual é a sua primeira nota?"))
nota2 = str(input("Qual é a sua segunda nota?"))
nota3 = str(input("Qual é a sua terceira nota?"))
nota4 = str(input("Qual é a sua quarta nota?"))

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
nota_total = ((nota1+nota2+nota3+nota4)/4)

if nota_total < 5:
    print("Você está reprovado.")
else:
    print("Você está aprovado.")