print("Hello world")

# Si posses hashtag es considera text i el programa no ho lleigeix

"""
Això és un bloc de codi i s'activa amb tres cometes
Anem a declarar variables:
Variables: entan en minúsculas
CONSTANTS: entan en majúscula
"""
enter_1 = 17 # És una variable entera
float_1 = 3 # Quan estem escrivint una funció i surt un color vol dir que no pot ser una funció, dons podem escriure (en aquest cas_1) per que sigui una funció
string_1 = 11

boolea_1 = True
boolea_2 = False

print(enter_1)
print(float_1)

#Operadors aritmètics
operació = enter_1 - float_1 + 4
print(f"operació té com a resultat: {operació}, i és de tipus: ·")

# Calculadora de productes.
import math
# lectura de les dades d'entrada


a = int(round(float(input("Digues un número: "))))

b = int(round(float(input("Digues un altre número: "))))

c = int(round(float(input("Digues un altre número: "))))

# càlcul del producte
x1 = (-b + (math.sqrt(b**2 - 4 * a * c))) / (2 * a)

x2 = (-b - (math.sqrt(b**2 - 4 * a * c))) / (2 * a)

print()

# escriptura de la dada de sortida
print('La x1 és', x1)
print('La x2 és', x2)