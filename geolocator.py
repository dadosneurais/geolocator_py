import requests

def public_ip():
    return requests.get('https://api.ipify.org').text # ip público

def get_location(ip):
    url = f'http://ipinfo.io/{ip}/json'
    data = requests.get(url).json()
    return data['loc']  # latitude e longitude

google_maps_url = f'https://www.google.com/maps?q={get_location(public_ip())}'

print(f'Meu IP público é: {public_ip()}')
print(f'URL do Google Maps: {google_maps_url}')
