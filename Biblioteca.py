biblioteca = []

print("=== GESTOR DE BIBLIOTECA v1.0 ===")

while True:
    #Mostrem el menú d'opcions
    print("\n----------------------------------------")
    print("SELECCIONA UNA OPCIÓ:")
    print("[1] Afegir un nou llibre")
    print("[2] Veure tots els llibres")
    print("[3] Sortir del programa")
    
    # Demanem l'opció a l'usuari
    opcio = input("\n> La teva opció: ")

    # Processem l'opció seleccionada
    if opcio == "1":
        print("\n--- AFEGINT NOU LLIBRE ---")
        nom_llibre = input("Nom del llibre: ")
        autor_llibre = input("Autor: ")
        
        # Comprobem que l'any estigui ben formatat
        while True:
            any_publicacio = input("Any de publicació: ")
            try:
                any_publicacio = int(any_publicacio)
                break
            except ValueError:
                print("ERROR: L'any ha de ser un número enter (ex: 1990).")

        nou_llibre = {
            "titol": nom_llibre,
            "autor": autor_llibre,
            "any": any_publicacio
        }

        biblioteca.append(nou_llibre)
        print("\n✅ Llibre afegit correctament!")
    # Veure tots els llibres
    elif opcio == "2":
        llibres_totals = len(biblioteca)
        if llibres_totals > 0:
            print(f"\n--- LLISTAT DE LLIBRES ({llibres_totals} llibres trobats) ---")
            for llibres in biblioteca:
                print(f" - '{llibres['titol']}' escrit per {llibres['autor']} ({llibres['any']})")
        else:
            print("\n  La biblioteca està buida.")
    #sortir del programa
    elif opcio == "3":
        print("\nGuardant dades...")
        print("Adéu! Fins la propera.")
        break  # Sortim del bucle i acabem el programa