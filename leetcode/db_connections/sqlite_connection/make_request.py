import requests

res =  requests.get(f"http://localhost:5000/api/inventory/products/01HD3XX3YRFEDSSF8VQRC304TY").text
print(f"RESPONSE: {res}")