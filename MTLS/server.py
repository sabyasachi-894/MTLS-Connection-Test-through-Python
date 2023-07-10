from flask import Flask, request
import ssl

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    # Load server certificate and private key
    server_cert = r'C:\Users\Lenovo\Desktop\MTLS Connection\MTLS\certificate.pem'
    server_key = r'C:\Users\Lenovo\Desktop\MTLS Connection\MTLS\key.pem'

    # Create SSL context with self-signed certificate and private key
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=server_cert, keyfile=server_key)

    # Run the app with SSL/TLS configured
    app.run(ssl_context=context, host='0.0.0.0', port=443)