Python qui peut interagir avec l'API ChatGPT directement dans le terminal :

```
import requests

# URL de l'API ChatGPT
url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

# Paramètres de la requête
headers = {"Authorization": "Bearer api_key", "Content-Type": "application/json"}
data = {"inputs": "Bonjour"}

# Fonction pour envoyer une requête à l'API et obtenir la réponse
def get_response(user_input):
    data["inputs"] = user_input
    response = requests.post(url, headers=headers, json=data)
    return response.json()[0]["generated_text"]

# Boucle principale pour interagir avec l'API dans le terminal
while True:
    user_input = input("Vous: ")
    response = get_response(user_input)
    print("ChatGPT: ", response)
```

Dans ce programme, nous utilisons la bibliothèque de requêtes Python pour envoyer une requête POST à l'API ChatGPT en utilisant l'URL et les paramètres spécifiés. Nous utilisons également un jeton d'
