# BerandaController.py
from flask import render_template, session
from app import db
from app.model.siswa import Siswa  # Model Siswa
from app.model.nilai import Nilai  # Model Nilai
from app.model.guru import Guru

def show_beranda():
    # Mengambil semua data siswa dari database
    siswa_list = Siswa.query.all()
    
    total_siswa = Siswa.query.count()
    total_guru = Guru.query.count()
    
    guru_nama = session.get('guru_nama', 'Guru')
    guru_nip = session.get('guru_nip', 'NIP')
    
    # Kirim data siswa ke template
    return render_template('index.html', siswa_list=siswa_list,total_siswa=total_siswa, total_guru=total_guru,guru_nama=guru_nama, guru_nip=guru_nip)

def show_data_siswa():
    # Mengambil semua data siswa dari database
    siswa_list = Siswa.query.all()
    
    total_siswa = Siswa.query.count()
    total_guru = Guru.query.count()
    
    # Kirim data siswa ke template
    return render_template('data_siswa.html', siswa_list=siswa_list,total_siswa=total_siswa, total_guru=total_guru)