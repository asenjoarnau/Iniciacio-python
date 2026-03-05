import math
pi = math.pi

# Definim les bases i altures en variables separades primer

# Creem les llistes pels triangle
triangle_1 = {"base": 10, "altura": 5},
triangle_2 = {"base": 8, "altura": 4},
triangle_3 = {"base": 12, "altura": 7}
# Creem la llista principal buida
triangles = []

# Afegim els triangles amb append
triangles.append(triangle_1)
triangles.append(triangle_2)
triangles.append(triangle_3)


# Fem el mateix per als cercles, variables separades
radi_1 = 3
radi_2 = 5
radi_3 = 10

# Creem la llista de cercles buida
cercles = []

# Els afegim amb append
cercles.append(radi_1)
cercles.append(radi_2)
cercles.append(radi_3)
# Text final per imprimir després de cada càlcul
text_final = "Hem acabat de calcular."

def calcul_area_triangle(llista_input):
    # Llista on guardarem resultats
    llista_resultats = []

    comptador = 1

    print("Iniciant la funció de càlcul de triangles...")
    print("-" * 30)

    # Bucle per recórrer la llista
    for element in llista_input:
        # Assignem variables temporals per claredat
        base = element[0]
        altura = element[1]

        print(f"Triangle número {comptador}:")
        print(f"Dada Base: {base}")
        print(f"Dada Altura: {altura}")

        # Fem el càlcul partit en dos passos
        resultat_area = 1/2 * (base * altura)

        # Guardem a la llista
        llista_resultats.append(resultat_area)

        print(f"Àrea calculada: {resultat_area}")
        print("-" * 30)

        # Sumem 1 al número
        comptador =+ 1

    print(text_final)
    print("\n")
    
    return llista_resultats

def calcul_area_cercle(llista_input):
    # Llista per guardar resultats
    resultats_cercles = []
    
    # Variable per comptar
    comptador =+ 1
    

    print("Iniciant la funció de càlcul de cercles...")
    print(f"Valor de PI: {pi}")
    print("-" * 30)

    for radi in llista_input:

        print(f"Cercle número {comptador}:")
        print(f"Dada Radi: {radi}")

        # Càlcul pas 1: fer el quadrat
        radi_quadrat = radi ** 2
        
        # Càlcul pas 2: multiplicar per PI
        area_final = pi * radi_quadrat

        # Guardem a la llista
        resultats_cercles.append(area_final)

        print(f"Radi al quadrat: {radi_quadrat}")
        print(f"Àrea calculada: {area_final}")
        print("-" * 30)

        # Sumem 1 al número
        comptador = comptador + 1

    print(text_final)
    print("\n")