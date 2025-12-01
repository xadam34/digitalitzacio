notes = {
    'Anna': [8, 9, 7],
    'Pau': [5, 6, 6],
    'Marta': [10, 9, 8]
}

for alumne, llista in notes.items():
    mitjana = sum(llista) / len(llista)
    print(f"{alumne} → {mitjana:.2f}")
