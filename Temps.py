import requests
import json

# --- CONFIGURACIÓ ---
api_key = "8d0c4705b9bf42cfa9a120340262801"

# Demanem a l'usuari la ciutat i el dia
ciutat = input("Quina ciutat vols consultar? ")
dia = int(input("Quin dia vols veure? (1=avui, 2=demà, 3=demà passat): "))

# Comprovem que el dia sigui vàlid
if dia < 1 or dia > 3:
    print("❌ Només puc mostrar dades dels propers 3 dies!")
    exit()

# --- PETICIÓ A L'API ---
url = "http://api.weatherapi.com/v1/forecast.json"

parametres = {
    "key": api_key,
    "q": ciutat,
    "days": 3,
    "aqi": "no",
    "alerts": "no"
}

resposta = requests.get(url, params=parametres)

# --- PROCESSAR DADES ---
if resposta.status_code == 200:
    dades = resposta.json()
    
    # Agafem el dia que ha demanat l'usuari (index 0 = avui, 1 = demà, etc.)
    dia_seleccionat = dades["forecast"]["forecastday"][dia - 1]
    
    # Extreure les dades que volem
    data = dia_seleccionat["date"]
    temp_max = dia_seleccionat["day"]["maxtemp_c"]
    temp_min = dia_seleccionat["day"]["mintemp_c"]
    temp_mitjana = dia_seleccionat["day"]["avgtemp_c"]
    vent = dia_seleccionat["day"]["maxwind_kph"]
    precipitacio = dia_seleccionat["day"]["totalprecip_mm"]
    
    # Guardar a fitxer
    with open("temps_girona.txt", "w", encoding="utf-8") as fitxer:
        fitxer.write(f"🌤️  Temps a {ciutat} - {data}\n")
        fitxer.write("=" * 40 + "\n\n")
        fitxer.write(f"Temperatura mitjana: {temp_mitjana}ºC\n")
        fitxer.write(f"Temperatura màxima: {temp_max}ºC\n")
        fitxer.write(f"Temperatura mínima: {temp_min}ºC\n")
        fitxer.write(f"Velocitat del vent: {vent} km/h\n")
        fitxer.write(f"Precipitació total: {precipitacio} mm\n")
    
    print(f"\n✅ Dades guardades a 'temps_girona.txt'")
    print(f"\n📊 Resum del dia {data}:")
    print(f"   🌡️  Temperatura: {temp_min}ºC - {temp_max}ºC (mitjana: {temp_mitjana}ºC)")
    print(f"   💨 Vent: {vent} km/h")
    print(f"   🌧️  Pluja: {precipitacio} mm")

else:
    print(f"❌ Error {resposta.status_code}: No he pogut obtenir les dades")
    print("Comprova que la ciutat estigui ben escrita o que tinguis connexió")