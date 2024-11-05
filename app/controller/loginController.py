from app import db
from app.model.admin import Admin
from flask import request, flash, redirect, url_for, session
from flask_login import login_user

def handle_login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        admin = Admin.query.filter_by(email=email).first()
        
        if admin:
            if admin.password == password:
                login_user(admin)
                # Simpan informasi guru ke session
                guru = admin.guru  # Dapatkan objek Guru
                session['guru_nama'] = guru.nama  # Ambil nama guru
                session['guru_nip'] = guru.nip  # Ambil NIP guru
                return redirect(url_for('beranda'))
            else:
                flash('Email atau password salah. Silahkan coba lagi.')
        else:
            flash('Email tidak ditemukan. Silahkan coba lagi.')
            
        return redirect(url_for('login'))
