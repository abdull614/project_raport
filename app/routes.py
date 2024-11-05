# routes.py
from flask import render_template
from app import app
from app.controller.BerandaController import show_beranda, show_data_siswa
from app.controller.NilaiController import daftar_nilai  # Mengimpor daftar_nilai dari NilaiController
from app.controller.NilaiController import input_nilai
from app.controller.SiswaController import tambah_siswa, edit_siswa, hapus_siswa
from app.controller.loginController import handle_login


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    result = handle_login()
    if result:
        return result
    return render_template('login.html')  # Import fungsi baru

@app.route('/input', methods=['GET', 'POST'])
def input_nilai_route():
    return input_nilai()

@app.route('/edit/<int:siswa_id>', methods=['GET', 'POST'])
def edit_siswa_route(siswa_id):
    return edit_siswa(siswa_id)


@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    return tambah_siswa()

@app.route('/hapus/<int:siswa_id>', methods=['POST'])
def hapus_siswa_route(siswa_id):
    return hapus_siswa(siswa_id)

