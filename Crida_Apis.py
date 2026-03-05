import requests
import json

# --- 1. CONFIGURACIÓ (Variables que haureu de fer interactives) ---
api_key = "8d0c4705b9bf42cfa9a120340262801"  # <--- Important: Posa la teva API Key!
ciutat = "Girona"
dies = 3 

# --- 2. PREPARACIÓ DE LA PETICIÓ ---
# La URL on preguntarem pel temps
base_url = "http://api.weatherapi.com/v1/forecast.json"

# Els paràmetres que enviem al servidor
parametres = {
    "key": api_key,
    "q": ciutat,
    "days": dies,
    "aqi": "no",
    "alerts": "no"
}

# --- 3. LA CRIDA (Request) ---
resposta = requests.get(base_url, params=parametres)

# --- 4. PROCESSAMENT I GUARDAT DE LA RESPOSTA ---
if resposta.status_code == 200:
    # Convertim la resposta (text) a un diccionari Python (JSON)
    dades = resposta.json()
    
    # Obrim (o creem) un fitxer de text per escriure-hi
    with open("temps_girona.txt", "w", encoding="utf-8") as fitxer:
        fitxer.write(f"🌍 Informació del temps a {ciutat}\n")
        fitxer.write("=" * 50 + "\n\n")
        
        # Temperatura actual
        temp_actual = dades["current"]["temp_c"]
        fitxer.write(f"Ara mateix estem a: {temp_actual}ºC\n\n")
        
        # Totes les dades en format JSON
        fitxer.write("DADES COMPLETES:\n")
        fitxer.write(json.dumps(dades, indent=4, ensure_ascii=False))
    
    print(f"✅ Informació guardada correctament a 'temps_girona.txt'")

else:
    with open("temps_girona.txt", "w", encoding="utf-8") as fitxer:
        fitxer.write(f"❌ Error {resposta.status_code}: No s'ha pogut obtenir la informació.\n")
    
    print(f"❌ Error {resposta.status_code}: Informació d'error guardada a 'temps_girona.txt'")