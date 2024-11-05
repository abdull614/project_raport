from flask import request, redirect, url_for, flash, render_template
from app import db
from app.model.siswa import Siswa
from app.model.kelas import Kelas
from app.model.nilai import Nilai

def tambah_siswa():
    if request.method == 'POST':
        id_siswa = request.form['id_siswa']
        nama = request.form['nama']
        nisn = request.form['nisn']
        tanggal_lahir = request.form['tanggal-lahir']
        jenis_kelamin = request.form['jenis-kelamin']
        alamat = request.form['alamat']
        id_kelas = request.form['tambah-kelas']  # Pastikan ini adalah ID kelas yang sesuai

        # Membuat objek Siswa
        siswa_baru = Siswa(
            id_siswa=id_siswa,
            nama=nama,
            nisn=nisn,
            tanggal_lahir=tanggal_lahir,
            jenis_kelamin=jenis_kelamin,
            alamat=alamat,
            id_kelas=id_kelas
        )

        try:
            db.session.add(siswa_baru)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

        return redirect(url_for('data_siswa'))  # Redirect ke halaman data siswa

    # Ambil daftar kelas untuk ditampilkan di dropdown
    kelas_list = Kelas.query.all()
    return render_template('tambah.html', kelas_list=kelas_list)

def edit_siswa(siswa_id):
    # Mengambil data siswa berdasarkan id
    siswa = Siswa.query.get(siswa_id)
    if siswa is None:
        # Jika siswa tidak ditemukan, redirect ke halaman data siswa
        return redirect(url_for('data_siswa'))

    if request.method == 'POST':
        # Mengupdate data siswa dengan data yang baru
        siswa.nama = request.form['nama']
        siswa.nisn = request.form['nisn']
        siswa.tanggal_lahir = request.form['tanggal-lahir']
        siswa.jenis_kelamin = request.form['jenis-kelamin']
        siswa.id_kelas = request.form['tambah-kelas']
        siswa.alamat = request.form['alamat']

        # Menyimpan perubahan ke database
        db.session.commit()
        return redirect(url_for('data_siswa'))  # Redirect setelah berhasil

    # Jika metode bukan POST, kita akan merender form edit dengan data yang sudah ada
    kelas_list = Kelas.query.all()  # Mengambil daftar kelas untuk dropdown
    return render_template('edit.html', siswa=siswa, kelas_list=kelas_list)

def hapus_siswa(siswa_id):
    # Hapus semua entri di tabel "nilai" yang terkait dengan siswa yang akan dihapus
    Nilai.query.filter_by(id_siswa=siswa_id).delete()
    db.session.commit()  # Pastikan untuk commit penghapusan ini sebelum lanjut ke penghapusan siswa

    # Lanjutkan penghapusan siswa
    siswa = Siswa.query.get(siswa_id)
    db.session.delete(siswa)
    db.session.commit()
    return redirect(url_for('data_siswa'))