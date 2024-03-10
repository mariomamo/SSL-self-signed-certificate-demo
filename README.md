# SSL certificate test in python
This is a simple python project which uses Flask as web server and a self signed certificate to make available https.

## Generate private key and public certificate
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:4096 \
  -keyout private_key.pem -out certificate.crt \
  -subj "/C=IT/ST=Region/L=City/O=Organization/CN=Domain" \
  -addext "subjectAltName = IP:192.168.1.20, IP:192.168.1.16, DNS:localhost"
```

## Create venv
```bash
python -m venv .venv
```

## Acivate venv
```bash
.\.venv\Scripts\activate
```

## Install python requirements
```bash
pip install -r requirements.txt
```

## Start flask server
```bash
.\.venv\Scripts\activate; python server.py
```

## Do request
```bash
.\.venv\Scripts\activate; python client.py
```
