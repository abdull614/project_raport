# routes.py
from flask import render_template
from app import app
from app.controller.BerandaController import show_beranda, show_data_siswa
from app.controller.NilaiController import daftar_nilai  # Mengimpor daftar_nilai dari NilaiController
from app.controller.NilaiController import input_nilai

@app.route('/')
def beranda():
    return show_beranda()

@app.route('/data_siswa')
def data_siswa():
    return show_data_siswa()

@app.route('/cetak')
def cetak():
    return render_template('cetak.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/login')
def login():
    return render_template('login.html')  # Import fungsi baru

@app.route('/input', methods=['GET', 'POST'])
def input_nilai_route():
    return input_nilai()

