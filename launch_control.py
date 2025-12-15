bateria = int(input("Quin nivell de bateria tens?: "))
vent = int(input("A quina velocitat va el vent?: "))
medic = input("És de nivell d'orgència mèdic?: ")

print("========================================")
print("[+] ECODRONE FLIGHT CONTROL v2.0")
print("========================================")
print("> DADES DE TELEMETRIA:")


estat_bateria = "AUTORITZAT"

if bateria > 20:
   print(f"Nivell de Bateria: [{bateria} %] OK")


elif bateria < 20:
      print(f"Nivell de Bateria: [{bateria} %] DENEGAT ")
      estat_bateria = "DENEGAT"


if vent < 50:
   print(f"Velocitat Vent: [{vent} km/h] Estable")

elif vent > 50 and medic == "si" or medic == "Si":
    print(f"Velocitat Vent: [{vent} km/h] OK")

else: print(f"Velocitat Vent: [{vent} km/h] DENEGAT")
estat_bateria = "DENEGAT"


print("—————————————-")
print("> ANALITZANT SISTEMES...")

if estat_bateria == "DENEGAT":
    print("»> ESTAT FINAL: [DENEGAT] ")

else: print("»> ESTAT FINAL: [AUTORITZAT] ")