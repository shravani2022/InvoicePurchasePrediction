from flask import Flask
from controllers.login_controller import login_bp

app = Flask(__name__)


app = Flask(__name__)
app.secret_key = "invoice_fraud_secret_key"

app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(debug=True)