import requests

url = "https://webhook.site/be4ff693-6193-43b3-86fd-f0caea05a772"

payload = {
    "plato": "pasta",
    "cantidad": 2
}
query_params = {
    "nombre": "Paco"
}

response = requests.post(url, data=payload, params=query_params)

print(response.status_code)