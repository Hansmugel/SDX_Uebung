import requests
import json

# Die Basis-URL deines Servers (ersetze dies mit der tatsächlichen URL)
base_url = "http://localhost:8080"

# Der spezifische Pfad des Endpunkts
endpoint = "/recipes"

# Vollständige URL
url = base_url + endpoint

# Die Daten für das neue Rezept
data = {
    "name": "Schokoladenkuchen",
    "description": "Ein reicher, feuchter Schokoladenkuchen",
    "ingredients": ["Zucker", "Mehl", "Kakaopulver", "Backpulver", "Eier", "Milch", "Pflanzenöl", "Vanilleextrakt", "kochendes Wasser"]
}

# Konvertieren des Python-Dictionarys in einen JSON-String
json_data = json.dumps(data)

# Setzen der HTTP-Header für die Anfrage
headers = {
    "Content-Type": "application/json"
}

# Senden der POST-Anfrage
response = requests.post(url, headers=headers, data=json_data)

# Überprüfen der Antwort
if response.status_code == 200:
    print("Erfolgreich gesendet!")
    print(response.json())  # Die Antwort des Servers anzeigen
else:
    print(f"Fehler beim Senden der Anfrage. Status-Code: {response.status_code}, Antwort: {response.text}")
