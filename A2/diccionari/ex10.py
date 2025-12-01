frase = input("Introdueix una frase: ")
paraules = frase.split()
freq = {}

for p in paraules:
    if p in freq:
        freq[p] += 1
    else:
        freq[p] = 1

print(freq)
