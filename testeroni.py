import requests
import json
import sys

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
print(json_data)
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
    sent = response.json()
else:
    print(f"Fehler beim Senden der Anfrage. Status-Code: {response.status_code}, Antwort: {response.text}")
    sys.exit(-1)

response = requests.get(url)

if response.status_code == 200:
    print("Hier sind die derzeitig gespeicherten Rezepte:")
    print(response.json())
    received=response.json()
else:
    print('Fehler beim Abrufen der Daten. Statuscode:', response.status_code)
    sys.exit(-1)

print(sent)
print(received)

sent_ingredients = sent[0]["ingredients"]
received_ingredients = received[0]["ingredients"]
if sent_ingredients[3] == received_ingredients[3]:
    print("Alles erfolgreich, senden und empfangen war perfekt!")
else:
    print("Irgendwas ist schief gegenagen?!")
    sys.exit(-1)