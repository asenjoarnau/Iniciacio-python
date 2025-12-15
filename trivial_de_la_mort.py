import time 

# ==============================================================================
# 1. CONFIGURACIÓ INICIAL (Això us ho dono fet per no perdre temps picant dades)
# ==============================================================================

banc_de_preguntes = [
    {
        "enunciat": "Quin és el planeta més gran del Sistema Solar?",
        "opcions": ["1. Mart", "2. Júpiter", "3. Terra"],
        "correcta": 2
    },
    {
        "enunciat": "Quant és 2 + 2 x 2?",
        "opcions": ["1. 6", "2. 8", "3. 4"],
        "correcta": 1
    },
    {
        "enunciat": "Quina extensió tenen els fitxers de Python?",
        "opcions": ["1. .pyt", "2. .pt", "3. .py"],
        "correcta": 3
    }
]  

# Variables d'Estat del joc
vides = 3
punts = 0
index_pregunta = 0 # Per saber per quina pregunta anem (0, 1, 2...)

print("😈 BENVINGUT AL TRIVIAL DE LA MORT 😈")
print(f"Comences amb {vides} vides. Bona sort...\n")


# ==============================================================================
# 2. BUCLE PRINCIPAL DEL JOC
# ==============================================================================

# TODO: Defineix el WHILE. 
# Pista: El joc ha de continuar MENTRE quedin vides (> 0) I l'índex sigui menor que el total de preguntes.
while vides > 0 and index_pregunta < len(banc_de_preguntes):

    # --------------------------------------------------------------------------
    # PAS A: Recuperar la informació
    # --------------------------------------------------------------------------
    # TODO: Crea una variable 'pregunta_actual' i assigna-li el diccionari que toca segons l'índex.
    
    preguntaactual = banc_de_preguntes[index_pregunta] 

    # --------------------------------------------------------------------------
    # PAS B: Mostrar per pantalla
    # --------------------------------------------------------------------------
    # TODO: Fes print de l'enunciat i de les opcions possibles.
    print(preguntaactual["enunciat"]) 
    for opcio in preguntaactual["opcions"]:
        print(opcio)  

    # --------------------------------------------------------------------------
    # PAS C: Demanar resposta a l'usuari (Validació)
    # --------------------------------------------------------------------------
    # TODO: Fes un bucle infinit amb TRY-EXCEPT per assegurar que l'usuari introdueix un NÚMERO enter.
    # Guarda la resposta en una variable.
    while True:
        try:
            resposta = int(input("Introdueix el número de la teva resposta: "))
            if resposta < 1 or resposta > len(preguntaactual["opcions"]):
                print("Si us plau, introdueix un número vàlid entre 1 i", len(preguntaactual["opcions"]))
                continue
            break
        except ValueError:
            print("Entrada no vàlida. Si us plau, introdueix un número enter.")

    # --------------------------------------------------------------------------
    # PAS D: Comprovar si ha encertat (Lògica del joc)
    # --------------------------------------------------------------------------
    # TODO: Fes un IF/ELSE comparant la resposta de l'usuari amb la 'correcta' del diccionari.
    # - Si encerta: Suma 10 punts i felicita'l.
    # - Si falla: Resta 1 vida i avisa'l de quantes li queden.
    if resposta == preguntaactual["correcta"]:
        punts += 10
        print("Correcte! Has guanyat 10 punts.")
    else:
        vides -= 1
        print(f"Incorrecte! Et queden {vides} vides.")

    # --------------------------------------------------------------------------
    # PAS E: Avançar
    # --------------------------------------------------------------------------
    # TODO: IMPORTANT! Incrementa l'índex per passar a la següent pregunta a la propera volta.
    index_pregunta += 1
    
    print("-" * 30) # Separador estètic entre preguntes


# ==============================================================================
# 3. FINAL DEL JOC
# ==============================================================================

# TODO: Fora del bucle, comprova com ha acabat la partida.
# - Si vides és 0 -> GAME OVER.
# - Si no -> ENHORABONA.
# Finalment, mostra els punts totals.

if vides == 0:
    print("GAME OVER! T'has quedat sense vides.")
else:
    print("ENHORABONA! Has superat el trivial.")