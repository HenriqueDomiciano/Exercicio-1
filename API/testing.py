import requests

BASE = 'http://127.0.0.1:5000/'
s = requests.Session()
s.auth = ('admin', 'suadmin')
response = s.get(BASE+'Country',params={'ISO':'BRA','is_vaccine':'cases'})
print(response.json())