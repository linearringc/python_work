import requests
response = requests.get("https://notebooklm.google/app")
if response.ok:
    print(response.text)
else:
    print('failed')