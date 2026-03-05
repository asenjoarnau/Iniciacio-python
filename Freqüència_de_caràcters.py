# El text que volem analitzar
text = input("Introdueix lletres al atzar: ")

# Passem tot el text a minúscules per no diferenciar majúscules de minúscules
text = text.lower()

# Creem l'alfabet manualment
alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Funció per comptar quantes vegades apareix una lletra al text
def comptar_lletres(text, lletra):
    comptador = 0
    for caracter in text:
        if caracter == lletra:
            comptador += 1
    return comptador

# Passem per cada lletra de l'alfabet
for lletra in alfabet:
    freq = comptar_lletres(text, lletra)
    
    # Només mostrem la lletra si apareix com a mínim un cop 1 vegada
    if freq > 0:
        barra = "█" * freq
        print(lletra.upper() + " | " + barra + " " + str(freq))