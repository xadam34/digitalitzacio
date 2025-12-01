paraula = input("Introdueix una paraula: ")
comptador = {}

for lletra in paraula:
    if lletra in comptador:
        comptador[lletra] += 1
    else:
        comptador[lletra] = 1

print(comptador)
