from flask import Flask
from controllers.login_controller import login_bp
from controllers.upload_controller import upload_bp

app = Flask(__name__)


app = Flask(__name__)
app.secret_key = "invoice_fraud_secret_key"

app.register_blueprint(login_bp)
app.register_blueprint(upload_bp)

if __name__ == '__main__':
    app.run(debug=True)