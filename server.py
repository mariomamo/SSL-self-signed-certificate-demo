from flask import Flask

app = Flask(__name__)

# Define SSL certificate and key file paths
CERT_FILE = "certificate.crt"
KEY_FILE = "private_key.pem"


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", ssl_context=(CERT_FILE, KEY_FILE))
