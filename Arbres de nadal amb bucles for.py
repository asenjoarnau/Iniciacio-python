import random

# 1. DEFINICIÓ DE COLORS (CONSTANTS)
RESET = "\033[0m"
VERD_ARBRE = "\033[92m" 
COLOR_TRONC = "\033[33m" 
BOLES = ["\033[91m", "\033[93m", "\033[94m"] 
ESTRELLA_DE_DALT = "\033[93m" 

print("\nCrea el teu arbre de Nadal decorat!🌲\n")

# 2. ENTRADA DE DADES
#Incorporem el try/except per assegurar que l'entrada és un enter
while True:
    try:
        n = int(input("Alçada de l'arbre (recomanat > 8): \n"))
        break
    except ValueError:
        print("L'alçadaa ha de ser un nombre enter!\n")

print("\n") 

# 3. DIBUIXAR L'ARBRE
# L'estrella a dalt (centrada simple)
print(" " * (n - 1) + "⭐️")

# 3.1 BUCLE PRINCIPAL (FILES)
for i in range(n):

    # A. NEU ESQUERRA 
    num_espais = n - 1 - i
    for k in range(num_espais):
        dau_neu = random.random()
        if dau_neu > 0.95: 
            print("❄️", end="")
        else:
            print(" ", end="")

    # B. Càlcul amplada de l'arbre
    num_elements = 2 * i + 1

    # C. L'ARBRE (Dibuixem la fila píxel a píxel)
    for j in range(num_elements):
        dau = random.random()
        if dau > 0.85: 
            color_bola = random.choice(BOLES)
            print(color_bola + "o" + RESET, end="")
        else:
            print(VERD_ARBRE + "*" + RESET, end="")

    # NEU DRETA
    # Fem exactament el mateix que a la part A
    for k in range(num_espais):
        dau_neu = random.random()
        if dau_neu > 0.95: 
            print("❄️", end="")
        else:
            print(" ", end="")
    # -------------------------------------------------

    # D. Final de fila: Salt de línia obligatori
    print()

# 3.2 EL TRONC
alçada_tronc = 2
marge_tronc = " " * (n - 2) 

for k in range(alçada_tronc):
    print(marge_tronc + COLOR_TRONC + "|||" + RESET)

print("\n\tBON NADAL!")