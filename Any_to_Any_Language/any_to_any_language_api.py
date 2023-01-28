import requests

url = "https://app.aimarketplace.co/api/marketplace/models/language-translation-05408f55/predict/"
payload={'data': open('Sample.csv','rb')}
headers = {'Authorization': 'Api-Key tAKNfH3U.IdwJ3YhHeslMW1ts3gs3TZom5Orqfk1c'}

response = requests.request("POST", url, headers=headers, files=payload)

print(response.text)