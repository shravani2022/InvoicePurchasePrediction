from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import pandas as pd

upload_bp = Blueprint('upload', __name__)

UPLOAD_FOLDER = "uploads"

@upload_bp.route('/upload_invoice')
def upload_invoice():
    return render_template('upload_invoice.html')


@upload_bp.route('/upload_invoice', methods=['POST'])
def upload_invoice_post():

    file = request.files['invoice_file']

    if file.filename == "":
        return "Please Select File"

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    filename = secure_filename(file.filename)

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)
    
    df = pd.read_excel(filepath)
    
    print("First 5 rows")
    df.head(5)
    
    print("Last 5 rows")
    df.tail(5)
    

    print("Saved at:", os.path.abspath(filepath))

    return redirect(url_for('upload.upload_invoice'))