nom = input("Introdueix el teu nom: ")

edat = int(input("Introdueix la teva edat: "))

pes = float(input("Introdueix la teva pes (kg): "))

altura = float(input("Introdueix la teva altura (m): "))

print()

print("---- Informe de salut ----")
print(f"Nom: {nom} {type(nom)}")
print(f"Edat: {edat} anys")
print(f"pes: {pes} kg")
print(f"Altura: {altura} m")

print()

imc = pes / altura**2
    
print(f"Índex de massa corporal (IMC): {imc}")   

if imc > 40:
    print("Classificació: Obsesitat III")

elif imc > 35:
    print("Classificació: Obsesitat II")

elif imc > 30: 
    print("Classificació: Obsesitat I")

elif imc > 25: 
    print("Classificació: Sobrepès")

elif imc > 18.5: 
    print("Classificació: Pes normal")

elif imc < 18.5: 
    print("Classificació: Pes baix")

print("--------------------------")