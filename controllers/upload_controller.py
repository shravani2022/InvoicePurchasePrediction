from flask import Blueprint, render_template, request, redirect, url_for,session
from werkzeug.utils import secure_filename
from database.db import mysqlconnection
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
    
    total_records  = len(df)
    
    conn = mysqlconnection()
    cursor = conn.cursor()
        #---------------------------
    # insert data in upload details
    #------------------------------
    
    cursor.callproc('USP_INSERT_UPLOAD',
    (
        filename,
        session['Username'],
        total_records,
        0,
        0,
        'Processing',
        'Excel Upload Started'
    ))
    
    upload_id = None

    for result in cursor.stored_results():
        row = result.fetchone()
        upload_id = row[0]

    print("Upload ID :", upload_id)
    
    for index,row in df.iterrows():
        
        print("-----------------")
        
        print("Row number",index + 1)
        
        print("Supplier Number :", row["Supplier Number"])
        print("Supplier Name :", row["Supplier Name"])
        print("Invoice Number :", row["Invoice Number"])
        print("Gross Total :", row["Gross Total"])

        break
    
    conn.commit()
    cursor.close()
    conn.close()    

    
    print("First 5 rows")
    print(df.head(5))
    
    print("Last 5 rows")
    print(df.tail(5))
    

    print("Saved at:", os.path.abspath(filepath))

    return redirect(url_for('upload.upload_invoice'))