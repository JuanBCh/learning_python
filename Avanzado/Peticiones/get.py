import requests

response = requests.get("https://api.github.com")
# print(response)
# print(response.headers)
# print(response.status_code)
# print(response.json())
# print(response.json()["current_user_url"])

response_2 = requests.get(
    "https://api.github.com/repositories",
    params={"q": "python"}
)

data = response_2.json()
# print(data.keys()) # No funciona