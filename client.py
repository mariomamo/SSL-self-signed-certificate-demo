import requests

session = requests.session()
CERT_FILE = "certificate.crt"

session.verify = CERT_FILE
response = session.get('https://localhost:5000/')
if response.ok:
    print(f"Request ok [{response.status_code}]")
else:
    print(f"Error in request [{response.status_code}]")
