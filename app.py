import requests

res = requests.get('https://gorest.co.in/public/v2/users')
print(res.json())