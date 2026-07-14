from flask import Blueprint, render_template, request, redirect, url_for, session
from database.db import mysqlconnection

login_bp = Blueprint('login', __name__)

@login_bp.route('/')
def home():
    return render_template('login.html')
    
@login_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = mysqlconnection()
    cursor = conn.cursor()
    
    cursor.callproc('USP_VALIDATE_LOGIN', (username, password))
    
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if user:
        session['UserID'] = user['UserID']
        session['Username'] = user['Username']
        session['Role'] = user['Role']

        return redirect(url_for('login.dashboard'))

    return render_template(
        'login.html',
        error="Invalid Username or Password"
    )

@login_bp.route('/dashboard')
def dashboard():
    
    if 'UserID' not in session:
        return redirect(url_for('login.home'))
    
    conn = mysqlconnection()
    cursor = conn.cursor()
        
    cursor.callproc('USP_DASHBOARD_SUMMARY')
    summary = cursor.fetchone()
        
    cursor.close()
    
    conn.close()

    return render_template('dashboard.html',username =  session['Username'],summary=summary)