from flask import render_template, redirect, url_for, request
from app import app, db
from app.model.nilai import Nilai
from app.model.siswa import Siswa
from app.model.mataPelajaran import MataPelajaran

@app.route('/daftar_nilai')
def daftar_nilai():
    # Mengambil semua data nilai dengan join ke tabel siswa dan mata pelajaran
    daftar_nilai = db.session.query(
        Siswa.nama.label("nama_siswa"),
        MataPelajaran.nama_pelajaran.label("mata_pelajaran"),
        Nilai.nilai_akhir.label("nilai")
    ).join(Nilai, Siswa.id_siswa == Nilai.id_siswa)\
     .join(MataPelajaran, MataPelajaran.id_mata_pelajaran == Nilai.id_mata_pelajaran)\
     .all()

    # Memproses data untuk ditampilkan per siswa
    siswa_nilai = {}
    for data in daftar_nilai:
        if data.nama_siswa not in siswa_nilai:
            siswa_nilai[data.nama_siswa] = {}
        siswa_nilai[data.nama_siswa][data.mata_pelajaran] = data.nilai

    return render_template('daftar_nilai.html', siswa_nilai=siswa_nilai)

@app.route('/input', methods=['GET', 'POST'])
def input_nilai():
    if request.method == 'POST':
        # Proses data input dari form
        for key, value in request.form.items():
            if value:
                # Format nama input: "<mata_pelajaran>_<id_siswa>"
                pelajaran, id_siswa = key.split('_')
                nilai = int(value)
                
                # Cari ID mata pelajaran berdasarkan nama pelajaran
                mata_pelajaran = MataPelajaran.query.filter_by(nama_pelajaran=pelajaran).first()
                
                if mata_pelajaran:
                    # Cek apakah nilai sudah ada
                    nilai_record = Nilai.query.filter_by(id_siswa=id_siswa, id_mata_pelajaran=mata_pelajaran.id_mata_pelajaran).first()
                    if nilai_record:
                        # Update nilai jika sudah ada
                        nilai_record.nilai_akhir = nilai
                    else:
                        # Buat nilai baru jika belum ada
                        new_nilai = Nilai(id_siswa=id_siswa, id_mata_pelajaran=mata_pelajaran.id_mata_pelajaran, nilai_akhir=nilai)
                        db.session.add(new_nilai)
        db.session.commit()
        return redirect(url_for('input_nilai'))
    
    # Query semua siswa dan mata pelajaran
    siswa_list = Siswa.query.all()
    mata_pelajaran_list = MataPelajaran.query.all()
    daftar_nilai = db.session.query(Nilai).all()
    
    # Struktur data nilai untuk diisi pada form
    nilai_dict = {(n.id_siswa, n.id_mata_pelajaran): n.nilai_akhir for n in daftar_nilai}
    
    return render_template('input.html', siswa_list=siswa_list, mata_pelajaran_list=mata_pelajaran_list, nilai_dict=nilai_dict)
