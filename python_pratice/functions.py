# Função para calcular o quadrado de um número

def quadrado(x):
  return x * x

# a função range() cria uma sequência de números 
for i in range(11):
  print(f"O quadrado de {i} é: {quadrado(i)}")

print("\n")
  
numero = int(input("um numero: "))
print(f"O quadrado de {numero} é: {quadrado(numero)} \n")