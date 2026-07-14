from flask import Blueprint, render_template, request, redirect, url_for, session
from database.db import mysqlconnection

upload_bp = Blueprint('upload',__name__)


@upload_bp.route('/upload_invoice')
def upload_invoice():
    return render_template('upload_invoice.html')


@upload_bp.route('/upload_invoice',method=['POST'])
def upload_invoice_post():
    
    file = request.files['invoice_file']
    
    print(file.filename)
    
    return "File Received Successfully"