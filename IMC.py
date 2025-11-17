nom = input("Introdueix el teu nom: ") # Basicament ensenya a pantalla la pregunta i es deixa un espall per respondre

edat = int(input("Introdueix la teva edat: ")) # En aquest li afegim el int perquè la resposta ha de ser un nombre real que es el que fa int 

pes = float(input("Introdueix la teva pes (kg): ")) # Aquí possem float perquè pot ser un numero enter o amb decimals

altura = float(input("Introdueix la teva altura (m): ")) # El mateix

print() # Aquest print el que fa és que deixa un espai en la sortida de dades

print("---- Informe de salut ----") # Bascament que aquest text en blau surti en pantalla
print(f"Nom: {nom}") # basicament el print es perque imprimeixi nom: x.  i els {} son per declarar nom com a variable
print(f"Edat: {edat} (tipo: {type(edat)})") # el mateix pero he afegit type(edat) perque em digui de quin tipus es la variable nom
print(f"Pes: {pes} kg (tipo: {type(pes)})") # el mateix
print(f"Altura: {altura} m (tipo: {type(altura)})") # el mateix

print() # Aquest print el que fa és que deixa un espai en la sortida de dades

imc = pes / altura**2  # declaro que imc = a pes / altura**2.  el **2 es per elevar un numero i ho pots fer amb qualsevol altre numero ex: **4, en aquest cas estaria elevat a 4
    
print(f"Índex de massa corporal (IMC): {imc:.2f}") # Basicament imprimeix l'índex de massa corporal {} son per declarar l variable imc. I els :2f és perque els dos punts son per indicar que donare instruccions de format, el .2 es perque el resultat sigui en dos decimals i la f es perque indica que el numero esta formatat en float, un numero decimal

if imc > 40:
    print("Classificació: Obsesitat III") # Bascicament es si imc es mes gran que 40 imprimeix que la seva classificació és de Obesitat III

elif imc > 35:
    print("Classificació: Obsesitat II")  # El mateix pero amb 35 i el elif es perque si no em mes gran que 40 miri si es mes gran que 35, i aixì repetidament fins que entri d'ins d'un interval

elif imc > 30: 
    print("Classificació: Obsesitat I") # mateix

elif imc > 25: 
    print("Classificació: Sobrepès") # mateix

elif imc > 18.5: 
    print("Classificació: Pes normal") # mateix

elif imc < 18.5: 
    print("Classificació: Pes baix")

print("--------------------------") # imprimeix aixo al final

"""
El que fa la ultima part es que si el imc és més gran de 40 imprimeix Classificació Obesitat III
I si no ho es que miri el d'abaix fins que trobi en quin interval està
"""

"""
El que fa aquest programa és calcular el Índex de massa corporal, el qual es poc dir si estas en pes baix, pes normal, sobre pes, etc...
"""