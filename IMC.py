nom = input("Introdueix el teu nom: ")

edat = int(input("Introdueix la teva edat: "))

pes = float(input("Introdueix la teva pes (kg): "))

altura = float(input("Introdueix la teva altura (m): "))

print()

print("---- Informe de salut ----")
print(f"Nom: {nom}")
print(f"Edat: {edat} (tipo: {type(edat)})")
print(f"Pes: {pes} kg (tipo: {type(pes)})")
print(f"Altura: {altura} m (tipo: {type(altura)})")

print()

imc = pes / altura**2


    
print(f"Índex de massa corporal (IMC): {imc:.2f}")   

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