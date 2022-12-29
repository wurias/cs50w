def calculaImc (peso, altura):
    return peso / (altura * altura)

peso = float(input("Informe seu Peso: "))
altura = float(input("Informe sua Altura: "))

imc = calculaImc(peso, altura)

if imc <= 18.5:
    print(f"\nSeu IMC é: {round(imc,2)} \nAbaixo do Peso Normal")
elif imc > 18.5 and imc <= 24.9:
    print(f"\nSeu IMC é: {round(imc,2)} \nPeso Normal")
elif imc > 24.9 and imc <= 29.9:
    print(f"\nSeu IMC é: {round(imc,2)} \nExcesso de Peso")
elif imc > 29.9 and imc <= 34.9:
    print(f"\nSeu IMC é: {round(imc,2)} \nObesidade Classe I")
elif imc > 34.9 and imc <= 39.9:
    print(f"\nSeu IMC é: {round(imc,2)} \nObesidade Classe II")
else:
    print(f"\nSeu IMC é: {round(imc,2)} \nObesidade Classe III")
