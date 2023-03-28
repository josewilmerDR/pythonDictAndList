par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"
par_lower = par.lower().replace(" ", "")

counts = {}
#your code go here:
for i in par_lower:
    if i ==" ": continue
    elif i in par_lower:
        counts[i] = par_lower.count(i)
print(counts)

#Other solution:
# Convertir el string a minúsculas y eliminar espacios
# par_lower = par.lower().replace(" ", "")

# # Crear un diccionario vacío para almacenar las frecuencias de las letras
# letter_count = {}

# # Contar las letras y sus frecuencias
# for letter in par_lower:
#     if letter in letter_count:
#         letter_count[letter] += 1
#     else:
#         letter_count[letter] = 1

# # Imprimir las frecuencias de las letras
# for letter, count in letter_count.items():
#     print(f"{letter}: {count}")
