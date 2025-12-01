
capital_pais = {
    "Espanya": "Madrid",
    "França": "París",
    "Itàlia": "Roma"
}

pais = input("Introdueix un país: ")

if pais in capital_pais:
    print(f"La capital de {pais} és {capital_pais[pais]}.")
else:
    print(f"No es troba la capital de {pais} en el diccionari.")    
