# SET (CONJUNTO)

# definidos, Os itens não podem ser alterados, 
# mas você pode removê-los itens e adicionar novos itens.

# criar conjunto vazio.
myset = set()

# conjuntos são escritos com colchetes.
myset = {"Andre", 10, 25, "Alfredo", 56, 99}
print(f"Conjunto MySet: {myset}")

# adcionar item ao conjunto (não aceita valor duplicado).
myset.add("Pedro")
myset.add("Pogba")
myset.add("Paulo")
myset.add("Pierre")
myset.add("Puskas")

print(f"Conjunto MySet: {myset}")

# método len() retorna o comprimento do conjunto.
lenght = len(myset)
print(f"Total de itens: {lenght}")

# método type() retorna o tipo primitivo.
print(f"Tipo: {type(myset)}")
num = 35
print(f"tipo {type(num)}")