import requests

url = "http://localhost:5000/predict"
data = {"composition": "Li2O"}
response = requests.post(url, json=data)
print(response.status_code)
print(response.text)