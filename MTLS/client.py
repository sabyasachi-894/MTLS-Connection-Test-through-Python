import requests
import ssl

# Load client certificate and private key
client_cert = r'C:\Users\Lenovo\Desktop\MTLS Connection\MTLS\certificate2.pem'
client_key = r'C:\Users\Lenovo\Desktop\MTLS Connection\MTLS\key2.pem'

# Make a request to the server with MTLS
url = 'https://localhost:443/'
response = requests.get(url, cert=(client_cert, client_key), verify=False)

print(response.text)