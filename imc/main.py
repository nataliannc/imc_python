'''
Crie um programa que calcula o IMC do usuário.
'''

#outra opção para converter str para float:
#peso = peso.replace(",",".")
#altura = altura.replace(",",".")

nome = input("Qual é o seu nome?")
peso = str(input("Qual é o seu peso?")).replace(',','.')
peso  = float(peso)

altura = str(input("Qual é a sua altura?")).replace(',','.')
altura = float(altura)

IMC = str(peso/(altura*altura)).replace(',','.')
IMC = float(IMC)

# :,.2f -> executa o imc, após a virgula, até a segunda casa decimal

if IMC < 18.5:
    print(f"O seu IMC é {IMC:,.2f}. Você está abaixo do peso normal. Coma mais um pouco.")
elif IMC > 18.5:
    print(f"O seu IMC é {IMC:,.2f}. Você está com o peso normal. Parabéns!")
elif IMC > 25.0:
    print(f"O seu IMC é {IMC:,.2f}. Você está com excesso de peso. Cuidado, coma menos!")
elif IMC > 30.0:
    print(f"O seu IMC é {IMC:,.2f}. Você está com obesidade classe I. Faça mais exercício físico.")
elif IMC > 35.0:
    print(f"O seu IMC é {IMC:,.2f}. Você está com obesidade classe II. Coma comida saúdavel e faça exercício físico.")
elif IMC >= 40.0:
    print(f"O seu IMC é {IMC:,.2f}. Você está com obesidade classe III. Atenção!!! Coma comida saúdavel e faça exercício físico.")