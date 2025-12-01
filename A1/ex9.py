list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

def ordenar_per_minim(llista):
    llista = llista.copy()
    resultat = []
    while llista:
        minim = min(llista)
        resultat.append(minim)
        llista.remove(minim)
    return resultat

print(ordenar_per_minim(list_num))
